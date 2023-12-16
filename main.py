import sys
import os
import subprocess, sys
from ui_main import *
from functions.ssh_utils import *
from functions.createBackup import *
from functions.restoreBackup import *
from functions.writeSiteConfig import *
import logging
from PySide6.QtCore import QObject, QThread
# IMPORT / GUI AND MODULES AND WIDGETS

# ///////////////////////////////////////////////////////////////

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui
        widgets.stackedWidget.setCurrentWidget(widgets.mainpage)
        
        self.thread={}

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
       # Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Backup Test Application"
        description = "Test Backup Project Description."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        widgets.buttonBack.clicked.connect(self.buttonClick)
        widgets.buttonNext.clicked.connect(self.buttonClick)
        widgets.buttonCancel.clicked.connect(self.buttonClick)
        widgets.buttonTestConnection.clicked.connect(self.buttonClick)
        widgets.button_preReq.clicked.connect(self.buttonClick)
        widgets.buttonSetBackupOptions.clicked.connect(self.buttonClick)
        widgets.button_StartBackup.clicked.connect(self.buttonClick)
        widgets.buttonStartRestore.clicked.connect(self.buttonClick)
        widgets.buttonTestConnectionHyp.clicked.connect(self.buttonClick)
        widgets.buttonRunCommand.clicked.connect(self.buttonClick)
        self.show()



    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

#Setup up Page#1 Buttons

        if btnName == "buttonTestConnection":
            ip = widgets.inputIPAddress.text()
            username = widgets.inputIUsername.text()
            self.password = widgets.inputPassword.text()
            port = widgets.inputPort.text()
            # Create a socket and connect to the target PC
            result, self.client = test_ssh_connection(ip, port, username, self.password)
            widgets.textOutputTestSSH.setPlainText(result)
            print(result, self.client)

#Setup up Page#2 Buttons
        #Check Pre-requisit
        if btnName == "button_preReq":
            print("Check Pre.req Pressed")
#           #command = "dpkg -s rear && dpkg -s nfs-common"
            command = "yum list installed rear && yum list installed nfs-utils" 
            output, error = run_command(self.client, command)
            print("output", output)
            print ("error", error)
            if error:
                widgets.plainTextEdit_3.setPlainText(error)
            else:
                widgets.plainTextEdit_3.setPlainText(output)

#Setup up Page#2 Buttons (Set Backup Options)
        if btnName =="buttonSetBackupOptions":
            if widgets.radioFullBackup.isChecked():
                self.backupType = "rear mkbackup"
            else:
                self.backupType = "rear mkrescue"
            if widgets.radioFullRecovery.isChecked():
                recoveryOption = 'ISO_RECOVER_MODE="unattended"'
            else:
                recoveryOption = '"#"'
            backupPath = widgets.inputBackupPath.text()
            print(self.backupType)
            print(recoveryOption)
            print(backupPath)
            widgets.plainTextBackupOptions.setPlainText(writeSiteConf(self.client, recoveryOption, self.password, backupPath))

#Setup up Page#5 Buttons (Start Backup )
        if btnName == "button_StartBackup":
            self.start_Creating_Backup()        







#Setup up Page#6 Buttons (Connect to HyperVisor )

        if btnName == "buttonTestConnectionHyp":
            ipHvp = widgets.inputIPAddressHyp.text()
            usernameHvp = widgets.inputIUsernameHyp.text()
            self.passwordHvp = widgets.inputPasswordHyp.text()
            portHvp = widgets.inputPort2.text() 
            # Create a socket and connect to the target PC
            result, self.clientHyp = test_ssh_connection(ipHvp, portHvp, usernameHvp, self.passwordHvp)
            widgets.textOutputTestSSHHvp.setPlainText(result)
            print(result, self.clientHyp)


#Setup up Page#7 Buttons (Start restore )
        if btnName == "buttonStartRestore":
            self.mediaPath = widgets.inputIRecoverymedia.text()
            self.vmName = widgets.inputIVmName.text()
            self.ramSize = widgets.inputIRamSize.text()
            self.diskSize = widgets.inputIDiskSize.text()
            if widgets.bootloaderUEFI.isChecked():
                self.bootloader = " --boot uefi"
            else:
                self.bootloader = ""
            
            widgets.stackedWidget.setCurrentWidget(widgets.page_8)
            widgets.textOutputRestoreLogs.clear()
            widgets.textOutputRestoreLogs.setPlainText("setting Up folder permissions.")
            output, error = setupFolderPerm(self.clientHyp, self.mediaPath, self.passwordHvp)
            if error:
                widgets.textOutputRestoreLogs.setPlainText(error)
            else:
                widgets.textOutputRestoreLogs.setPlainText(output)     
            self.start_vm_restore()        
  


        #Run Command
        if btnName =="buttonRunCommand":
            command = widgets.inputCommand.text()
            print(self.client)
            output, error = run_command(self.client, command)
            print(output, error)
            widgets.outputCommand.setPlainText(output)
        
        #Check Pre-requisit
        if btnName == "button_preReq":
            print("Check Pre.req Pressed")
            command = "dpkg -s rear && dpkg -s nfs-common" 
            output, error = run_command(self.client, command)
            print("output", output)
            print ("error", error)
            if error:
                widgets.plainTextEdit_3.setPlainText(error)
            else:
                widgets.plainTextEdit_3.setPlainText(output)
        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')

#Setup up Navigation Buttons

        if btnName == "buttonNext":
            print("Next Button Clicked")
            widgetname = (widgets.stackedWidget.widget(widgets.stackedWidget.currentIndex())).objectName()
            print (widgetname)
            if widgetname == "mainpage":
                widgets.stackedWidget.setCurrentWidget(widgets.page_1)
                widgets.buttonBack.setEnabled(True)
            elif widgetname == "page_1":
                widgets.stackedWidget.setCurrentWidget(widgets.page_2)
            elif widgetname == "page_2":
                #command = "dpkg -s rear && dpkg -s nfs-common" 
                #output, error = run_command(self.client, command)
                #if error: 
                    #widgets.plainTextEdit_3.setPlainText(error)
                #else:
                    widgets.stackedWidget.setCurrentWidget(widgets.page_4)
            elif widgetname == "page_4":
                widgets.stackedWidget.setCurrentWidget(widgets.page_5)
            elif widgetname == "page_5":
                widgets.stackedWidget.setCurrentWidget(widgets.page_6)
            elif widgetname == "page_6":
                widgets.stackedWidget.setCurrentWidget(widgets.page_7)
            elif widgetname == "page_7":
                widgets.stackedWidget.setCurrentWidget(widgets.page_8)
            elif widgetname == "page_8":
                widgets.stackedWidget.setCurrentWidget(widgets.page_last)


        if btnName == "buttonBack":
            widgetname = (widgets.stackedWidget.widget(widgets.stackedWidget.currentIndex())).objectName()
            print (widgetname)
            if widgetname == "page_1":
                widgets.stackedWidget.setCurrentWidget(widgets.mainpage)
                widgets.buttonBack.setEnabled(False)
            elif widgetname == "page_2":
                widgets.stackedWidget.setCurrentWidget(widgets.page_1)
            elif widgetname == "page_4":
                widgets.stackedWidget.setCurrentWidget(widgets.page_2)
            elif widgetname == "page_5":
                widgets.stackedWidget.setCurrentWidget(widgets.page_4)
            elif widgetname == "page_6":
                widgets.stackedWidget.setCurrentWidget(widgets.page_5)
            elif widgetname == "page_7":
                widgets.stackedWidget.setCurrentWidget(widgets.page_6)
            elif widgetname == "page_8":
                widgets.stackedWidget.setCurrentWidget(widgets.page_7)
            elif widgetname == "page_last":
                widgets.stackedWidget.setCurrentWidget(widgets.page_8)


        if btnName == "buttonCancel":
            print("buttonCancel Button Clicked")



    def start_Creating_Backup(self):

        self.thread['run_rear_backup'] = run_rear_backup(self.client, self.backupType, self.password)
        self.thread['run_rear_backup'].start()
        self.thread['run_rear_backup'].write_signal.connect(self.write)
        self.thread['run_rear_backup'].finished_signal.connect(self.finished)

        widgets.button_StartBackup.setEnabled(False)
        widgets.textOutputBackupLogs.clear()
        widgets.textOutputBackupLogs.setPlainText("Rear Backup is Starting now.....")
        
    def start_vm_restore(self):
        self.thread['vmRestore'] = vmRestore(self.clientHyp, self.mediaPath, self.vmName, self.ramSize, self.diskSize, self.passwordHvp, self.bootloader)
        self.thread['vmRestore'].start()
        self.thread['vmRestore'].write_signal.connect(self.write)
        self.thread['vmRestore'].finished_signal.connect(self.finished)

        widgets.buttonStartRestore.setEnabled(False)
        widgets.textOutputRestoreLogs.setPlainText("vm Restore is Starting now.....")
        

    def stop_thread_1(self):
        self.thread['run_rear_backup'].stop()
    def stop_thread_1(self):
        self.thread['vmRestore'].stop()


    def write(self, data):
        index = self.sender().__class__.__name__
        print(index + ': ' + data)
        if index == 'run_rear_backup':
            widgets.textOutputBackupLogs.appendPlainText( data + '\n')
        if index == 'vmRestore':
            widgets.textOutputRestoreLogs.appendPlainText( data + '\n')

    def finished(self):
        index = self.sender().__class__.__name__
        if index == 'run_rear_backup':
            self.write('Backup Thread Completed.')
            widgets.button_StartBackup.setEnabled(True)
        if index == 'vmRestore':
            self.write('Restore Thread Completed.')
            widgets.buttonStartRestore.setEnabled(True)







if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    logging.debug("Qt event loop started")

    sys.exit(app.exec_())
