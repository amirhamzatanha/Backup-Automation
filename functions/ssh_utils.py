import threading
import paramiko

def test_ssh_connection(ip, port, username, password):
    result = ""
    client = paramiko.SSHClient()
    def ssh_connection_thread():
        nonlocal result
        try:
            # Create SSH client
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # Connect to the target PC
            client.connect(ip, port=port, username=username, password=password)
            result = "Connection successful"
        except paramiko.AuthenticationException:
            result = "Authentication failed"
        except paramiko.SSHException as e:
            result = f"SSH error: {str(e)}"
        except Exception as e:
            result = f"An error occurred: {str(e)}"
    connection_thread = threading.Thread(target=ssh_connection_thread)
    connection_thread.start()
    connection_thread.join()
    return (result,client)

def run_command (ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    output = stdout.read().decode().strip()
    error = stderr.read().decode().strip()
    return output, error
    
