
from os import write

from PySide6 import QtCore
class vmRestore(QtCore.QThread):

    write_signal = QtCore.Signal(str)
    finished_signal = QtCore.Signal()
    def __init__(self, client, mediaPath, vmName, ramSize, diskSize, password, bootloader):
        super(vmRestore, self).__init__()
        self.client = client
        self.mediaPath = mediaPath
        self.vmName =  vmName
        self.ramSize = ramSize
        self.diskSize = diskSize
        self.password = password
        self.bootloader = bootloader

    
    def run(self):
        self.write_signal.emit('Starting VM Restore')

        virt_install_command = 'echo '+ self.password + ' | sudo -S ' + 'virt-install -d --name ' +  self.vmName + ' --memory ' + str(self.ramSize)+ ' --disk size='+ self.diskSize + ' --cdrom '+ self.mediaPath +' --os-type linux --os-variant generic' + self.bootloader
        channel = self.client.get_transport().open_session(timeout=5)

        try:
            channel.exec_command(virt_install_command)
            RECV_SIZE = 1024
            while not channel.closed:
                if channel.recv_ready():
                    stdout_data = channel.recv(RECV_SIZE).decode('utf-8')
                    self.write_signal.emit(stdout_data)
                    print("Stdout_data:")
                    print(stdout_data, end='')
                if channel.recv_stderr_ready():
                    stderr_data = channel.recv_stderr(RECV_SIZE).decode('utf-8')
                    self.write_signal.emit(stderr_data)
                    print("Stderr_data:")
                    print(stderr_data, end='')

            code = channel.recv_exit_status()
            if code == '0':
                self.write_signal.emit("Restore is Successful")
            else:
                self.write_signal.emit("")

            self.finished_signal.emit()
            print(f"Exit code: {code}")
        except Exception as inner_exception:
            print(f"Inner Error: {str(inner_exception)}")
        finally:
            channel.close()
    def stop(self):
        self.write_signal.emit('Stopping VM Restore Thread')
        self.finished_signal.emit()
        self.terminate()


# Reference https://github.com/MystixCode/QThreads_Example/blob/main/QThreads_Example