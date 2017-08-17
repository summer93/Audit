import os,sys
import paramiko
#
# t = paramiko.Transport(('192.168.11.108',22))
# t.connect(username='jimmy',password='jimmy123456')
# sftp = paramiko.SFTPClient.from_transport(t)
# sftp.get('/home/jimmy/log.log','D:/log.log')
# t.close()


filepath = '/home/jimmy/teste.log'

print(os.path.basename(filepath))