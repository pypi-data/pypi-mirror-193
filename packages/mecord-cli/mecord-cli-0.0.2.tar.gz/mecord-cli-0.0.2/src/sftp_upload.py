import paramiko
import os
import stat

# 判断sftp服务端中文件路径是否存在，若不存在则创建
def create_dir(sftp,remoteDir):
    try:
        if stat.S_ISDIR(sftp.stat(remoteDir).st_mode): # 如果remoteDir存在且为目录，则返回True
            pass
    except Exception as e:
        sftp.mkdir(remoteDir)

def sftp_upload(sftp,localDir,remoteDir):
    if os.path.isdir(localDir): # 判断本地localDir是否为目录
        for file in os.listdir(localDir):
            remoteDirTmp=os.path.join(remoteDir,file)
            localDirTmp=os.path.join(localDir,file)
            if os.path.isdir(localDirTmp): # 如果本地localDirTmp为目录，则对远程sftp服务器进行判断
                create_dir(sftp,remoteDirTmp) # 判断sftp服务端文件目录是否存在,若不存在则创建
            sftp_upload(sftp,localDirTmp,remoteDirTmp)
    else:
        sftp.put(localDir,remoteDir)

def upload(localDir, remoteDir):
    host = "ftp://192.168.3.220/1TB01/data/video/"#sftp主机 
    port = 21 #端口
    username = "xinyu100" #sftp用户名
    password = "xinyu100.com"  # 密码
    sf = paramiko.Transport((host,port))
    sf.connect(username = username,password = password)
    sftp = paramiko.SFTPClient.from_transport(sf)
    sftp_upload(sftp,localDir,remoteDir)
    sf.close()