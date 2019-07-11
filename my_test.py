import rsa

if __name__ == '__main__':
    # (pub_key, private_key) = rsa.newkeys(1024)
    # print(pub_key)
    # print(private_key)
    # pub = pub_key.save_pkcs1()
    # with open('id_rsa.pub', 'wb')as f:
    #     f.write(pub)
    #
    # private = private_key.save_pkcs1()
    # with open('id_rsa', 'wb') as f:
    #     f.write(private)
    import re
    p = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if re.match(p, '0.0.0.0'):
        print(1)
    else:
        print(0)

    # from urllib.parse import  unquote
    #
    # a = unquote('%E6%96%B0%E5%8A%A0%E5%8D%B7%20(F%3A)%2Ftif_images%2F00517837.mrxs')
    # print(a)

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
