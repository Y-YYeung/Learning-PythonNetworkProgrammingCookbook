# /usr/bin/python3

# 通过端口获取服务名

import socket


def find_service_name():
    protocolName = 'tcp'
    for port in [80, 25, 8080]:
        print("Port %s => service name: %s" % (port, socket.getservbyport(port, protocolName)))

    print("Port: %s => service name: %s" % (53, socket.getservbyport(53, 'udp')))

if __name__ == "__main__":
    find_service_name()
