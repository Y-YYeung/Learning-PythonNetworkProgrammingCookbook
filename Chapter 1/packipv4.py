# /usr/bin/python3

# 将 ipv4 地址转换成不同的格式

from binascii import hexlify  # 这里是引入了函数，以16进制表示2进制
import socket


def packipv4(ip):
    packed_ip_address = socket.inet_aton(ip)
    print("The low level format of this %s is: %s" % (ip, str(hexlify(packed_ip_address))))


if __name__ == "__main__":
    ip = input("input a ipv4 address: ")
    packipv4(ip)
