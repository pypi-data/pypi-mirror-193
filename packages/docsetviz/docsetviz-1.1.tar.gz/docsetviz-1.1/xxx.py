import paramiko

tran = paramiko.Transport(('10.110.156.92', 22))  # 获取 Transport 实例

tran.connect(username='yannan1', password='yannan12')  # 连接 SSH 服务端

sftp = paramiko.SFTPClient.from_transport(tran)  # 创建 SFTP 实例

sftp.get(remotepath='/mnt/cephfs/data/dataset/global_wheat_challenge_2021/test.ds',
         localpath='data/global_wheat_challenge_2021.ds')  # 下载文件