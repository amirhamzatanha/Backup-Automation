
import os
def writeSiteConf(ssh_client, recoveryOption, password, backupPath):
    # Remote file path to replace
    remote_file_path = '/etc/rear/site.conf'
    try:
        # Create an SSH shell session if not already created
        ssh_session = ssh_client.invoke_shell()
        # Send commands to edit the file with 'vi' editor
       #nfslocation = 
        commands = [
            f"echo {password} | sudo -S vi {remote_file_path}",
            ":set fileformat=unix",  # Ensure Unix line endings
            ":%d",  # Delete all lines
            "i",  # Enter insert mode in 'vi'
            'OUTPUT=ISO',
            'OUTPUT_URL=nfs://' + backupPath,
            'BACKUP=NETFS',
            'BACKUP_URL=nfs://' + backupPath,
            'BACKUP_PROG_EXCLUDE=("${BACKUP_PROG_EXCLUDE[@]}" "/media" "/var/tmp" "/var/crash" "/nfsshare")',
            'USER_INPUT_TIMEOUT=5',
            'USER_INPUT_INTERRUPT_TIMEOUT=2',
            'ISO_DEFAULT="automatic"',
            'USE_DHCLIENT="yes"',
            recoveryOption,  # Insert the new content
            "\x1B",  # Send the Escape key to exit insert mode
            ":wq",  # Save and exit
        ]
        # Send commands to the remote shell
        for command in commands:
            ssh_session.send(command + "\n")

        # Wait for the command to complete
        while not ssh_session.recv_ready():
            pass

        print(f"File {remote_file_path} replaced successfully.")
        return f"File {remote_file_path} replaced successfully."

    except Exception as e:
        print(f"Error: {str(e)}")
        return f"Error: {str(e)}"

# Example usage:
# Replace 'ssh_client' with your existing SSH client instance
# Example recoveryOption:
# recoveryOption = 'SOME_OPTION="value"'

# writeSiteConf(ssh_client, "type", "path", recoveryOption)




def setupFolderPerm (socket, mediaPath, passwd):
    try:
        folder_path = os.path.dirname(mediaPath)
        stdin, stdout, stderr = socket.exec_command("echo "+ passwd +" | sudo -S chmod -R a+rwx "+ folder_path + "\n")
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        return output, error
        
    except Exception as e:
        return str(e)
