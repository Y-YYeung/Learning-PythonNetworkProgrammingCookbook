# /usr/bin/python3

# 根据主机名字获取 IP 地址

import socket


def get_remote_machine_info():
    remote_host = input("Input a host name: ")
    try:
        print("IP address of remote host %s is: %s" % (remote_host, socket.gethostbyname(remote_host)))
    except socket.error as e:
        print("%s: %s" % (remote_host, str(e)))


if __name__ == "__main__":
    get_remote_machine_info()
