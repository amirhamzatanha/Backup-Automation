
from os import write

from PySide6 import QtCore
class run_rear_backup(QtCore.QThread):

    write_signal = QtCore.Signal(str)
    finished_signal = QtCore.Signal()
    def __init__(self, client, backupType, password):
        super(run_rear_backup, self).__init__()
        self.client = client
        self.backupType = backupType
        self.password = password

    def run(self):
        self.write_signal.emit('sudo run_rear_backup running')

        cmd = 'echo '+ self.password + ' | sudo -S ' + self.backupType + ' -d\n'
        command = "cat /etc/rear/site.conf"
        channel = self.client.get_transport().open_session(timeout=5)
        try:
            channel.exec_command(cmd)
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
                self.write_signal.emit("Backup is Successful")
            else:
                self.write_signal.emit("E..")

            self.finished_signal.emit()
            print(f"Exit code: {code}")
        except Exception as inner_exception:
            print(f"Inner Error: {str(inner_exception)}")
        finally:
            channel.close()
    def stop(self):
        self.write_signal.emit('Stopping thread1')
        self.finished_signal.emit()
        self.terminate()