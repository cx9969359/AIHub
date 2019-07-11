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


def get_id_rsa():
    """
    本地生成公钥,私钥
    :return:
    """
    (pub_key, private_key) = rsa.newkeys(1024)
    str_pub_key = pub_key.save_pkcs1()
    str_private_key = private_key.save_pkcs1()
    # 写入.ssh文件中
    with open('id_rsa.pub', 'wb')as f:
        f.write(str_pub_key)
    with open('id_rsa', 'wb') as f:
        f.write(str_private_key)
