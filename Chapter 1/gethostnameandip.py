# /usr/bin/python3

import socket


def print_machine_network_configuration():
    # 获取所在主机或本地主机的名字
    host_name = socket.gethostname()
    # 通过主机名字获取该主机的 IP 地址
    ip_address = socket.gethostbyname(host_name)
    print("Host name: %s" % host_name)
    print("IP address: %s" % ip_address)


if __name__ == "__main__":
    print_machine_network_configuration()
