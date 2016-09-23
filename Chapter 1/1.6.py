# 主机字节序列和网络字节序列之间的转换

import socket


def convert_integer():
    data = 10
    # 32 bits
    print("Original: %s => Long host byte order: %s, Network byte order: %s"
        % (data, socket.ntohl(data), socket.htonl(data)))
    # 16 bits
    print("Original: %s => Short host byte order: %s, Network byte order: %s"
        % (data, socket.ntohs(data), socket.htons(data)))


if __name__ == "__main__":
    convert_integer()
