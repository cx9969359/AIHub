import rsa


class SSHService():

    def get_pub_and_private_key(self):
        """
        生成公钥，私钥
        :return:
        """
        (pub_key, private_key) = rsa.newkeys(1024)
        str_pub_key = pub_key.save_pkcs1()
        str_private_key = private_key.save_pkcs1()
        # 写入pem格式文件
        with open('id_rsa.pub', 'wb')as f:
            f.write(str_pub_key)
        with open('id_rsa', 'wb') as f:
            f.write(str_private_key)

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
