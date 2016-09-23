# /usr/bin/python3

# 设定并获取默认的套接字超时时间

import socket


def test_socket_timeout():
    # 创建一个套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 获取默认超时时间
    print("Default socket timeout: %s" % s.gettimeout())
    # 设置超时时间
    s.settimeout(100)
    print("Current socket timeout: %s" % s.gettimeout())

if __name__ == "__main__":
    test_socket_timeout()
