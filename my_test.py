import rsa

if __name__ == '__main__':
    # (pub_key, private_key) = rsa.newkeys(2048)
    # print(pub_key)
    # print(private_key)
    # pub = pub_key.save_pkcs1()
    # import os
    # if not os.path.isdir('f:/.ssh'):
    #     os.makedirs('f:/.ssh')
    # with open('f:/.ssh/id_rsa.pub', 'wb')as f:
    #     f.write(pub)
    #
    # private = private_key.save_pkcs1()
    # with open('f:/.ssh/id_rsa', 'wb') as f:
    #     f.write(private)
    import os
    ssh_path_list = os.listdir('C:/Users/Chang/.ssh')
    print(ssh_path_list)
    # 使用paramiko
    # ssh = paramiko.SSHClient()
    # print(ssh)
    #
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname='192.168.23.23', port=22, username='root', password='1.23456')
    # cmd = 'ps'
    # stdin, stdout, stderr = ssh.exec_command(cmd)
    # result = stdout.read()
    # if not result:
    #     result = stderr.read()
    # ssh.close()
    # print(result.decode())
    #
    # transport = paramiko.Transport(('192.168.23.23',22))
    # transport.connect(username='root', password='1.23456')
    # print(transport)
    # sftp = paramiko.SFTPClient.from_transport(transport)
    # sftp.get('/home/n2n/README.md', 'F:/n2n.txt')
    # transport.close()
