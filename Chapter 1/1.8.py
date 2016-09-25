
# 处理套接字错误

import sys
import socket
import argparse
import pprint


def main():
    # 配置命令行参数转换
    parser = argparse.ArgumentParser(description='Socket Error Examples')
    parser.add_argument('--host', action="store", dest='host', required=False)
    parser.add_argument('--port', action="store", dest="port", type=int, required=False)
    parser.add_argument('--file', action="store", dest="file", required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # 创建 socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(30)
    except socket.error as e:
        pprint.pprint("Error creating socket: %s" % e)
        sys.exit(1)

    # 连接 socket
    try:
        s.connect((host, port))
    except socket.gaierror as e:  # 地址相关错误
        pprint.pprint("Address-related error connecting to server: %s" % e)
        sys.exit(1)
    except socket.error as e:
        pprint.pprint("Connection error: %s" % s)
        sys.exit(1)

    # 发送数据
    try:
        # Python3 中需要将字符串 encode 一下
        s.sendall(("GET %s HTTP/1.0\r\n\r\n" % filename).encode())
    except socket.error as e:
        pprint.pprint("Error sending data: %s" % e)
        sys.exit(1)

    # 接收数据
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            pprint.pprint("Error receiving data: %s" % e)
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(str(buf) + "\n")
        # pprint.pprint(buf)


if __name__ == "__main__":
    main()
