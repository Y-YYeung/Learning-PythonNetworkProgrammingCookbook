# SNTP 客户端 Simple Network Time Protocol

import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org" # 服务器地址
TIME1970 = 2208988800 # 指 1970.1.1 在 Python 3 中，所有 Integer 都为 long

def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 使用 UDP socket
    data = '\x1b' + 47 * '\0'
    client.sendto(data.encode(), (NTP_SERVER, 123))
    (data, address) = client.recvfrom(1024)
    if data:
        print("Response received from: " + str(address))
    t = struct.unpack('!12I', data)[10] # 将二进制数据转换，所需数据为 11th 元素
    t -= TIME1970 # 减去 TIME1970 得到真正的当前时间
    print("\tTime = %s" % time.ctime(t))

if __name__ == "__main__":
    sntp_client()
