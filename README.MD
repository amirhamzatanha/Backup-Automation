#################################################################
######                                                    #######
######            Pre-Requisites                          #######
######                                                    #######
#################################################################

1. Install NFS on both machines
    yum install -y nfs-utils
2. NFS Share should be accessible on both Source and Destination machines. 
    assumed that the NFS server is installed anywhere and accessible through both machines. 
3. on Source Machine install rear genisoimage syslinux
    yum install rear genisoimage syslinux
    or
    apt install rear genisoimage syslinux

4. install python 3.x and pyside 6 to run the code. 
    pip install PySide6
    https://pypi.org/project/PySide6/
    
    from the root directory run py ./main.py
