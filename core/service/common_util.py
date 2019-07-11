import os
import re

import rsa


def check_IP(IP):
    """
    正则校验IP
    :param IP:
    :return:
    """
    p = re.compile(r'^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if re.match(p, IP):
        return True
    else:
        return False


def generate_id_rsa():
    """
    本地生成公钥,私钥
    :return:
    """
    # 判断本地是否已经存在公钥私钥
    ssh_path_list = os.listdir('/root/.ssh')
    if 'id_rsa.pub' and 'id_rsa' in ssh_path_list:
        # 将id_rsa.pub通过ssh-copy-id发送到远程客户端
        pass
    else:
        # 生成本地ssh
        (pub_key, private_key) = rsa.newkeys(2048)
        str_pub_key = pub_key.save_pkcs1()
        str_private_key = private_key.save_pkcs1()
        # 写入.ssh文件中
        if not os.path.isdir('/root/.ssh'):
            os.makedirs('/root/.ssh')
        with open('/root/.ssh/id_rsa.pub', 'wb')as f:
            f.write(str_pub_key)
        with open('id_rsa', 'wb') as f:
            f.write(str_private_key)
