# Indexes

## 打印设备名和 IP 地址 gethostnameandip
- 所用函数

```py
socket.gethostname() # 获取所在主机或本地主机的名字
socket.gethostbyname("<host name>") # 通过主机名字获取主机 IP 地址
```

## 获取远程设备的 IP 地址 getremotehostnameip
- 所用函数

```py
socket.gethostbyname("<host name>") # 与上面相同
```

## 将 IPv4 地址转换成不同的格式 packipv4
- 使用底层网络函数，有时需要将 IP 地址转换成打包后的 32 位二进制格式
- 所用函数

```py
import socket
socket.inet_aton("<ip string>") # 将 IP 地址字符串打包
socket.inet_ntoa("<packed ip>") # 将打包后的 IP 地址解包

from binascii import hexlify
hexlify("<binary data>") # 将二进制数据以十六进制表示
```

## 通过指定的端口和协议找到服务名
- 要找到网络服务，需要知道服务运行在 TCP 或 UDP 协议的哪个端口上
- 所用函数

```py
import socket
socket.getservbyport(<port>, "<protocol name>") # 通过端口和协议名称，获取服务的名字 
```

## 主机字节序和网络字节序之间相互转换 1.6
- 编写底层网络应用时，有时需要处理通过电缆在两台设备之间传送的底层数据。需要把主机操作系统发出的数据转换成网络格式或逆向转换
- 所用函数

```py
from socket
socket.ntohl(data) # 网络字节序 -> 长整形主机字节序
socket.htonl(data) # 主机字节序 -> 长整形网络字节序

socket.ntohs(data) # 网络字节序 -> 短整形主机字节序
socket.htons(data) # 主机字节序 -> 短整形网络字节序
```
## 设定并获取默认的套接字超时时间 1.7
- 获取或设置套接字超时时间
- 所用函数

```py
from socket
socket.socket(socket.AFINET, socekt.SOCK_STREAM) # 创建一个基于 TCP 协议，IP 地址为 IPv4 类型的套接字对象

# <[Class]> 表示 Class 对象的一个实例
<[socket]>.gettimeout() # 获取超时时间，默认为 None
<[socekt]>.settimeout(<timeout>) # 设置超时时间
```

## 处理 socket 错误
- 所用函数

```py
import socket
<[socket]>.sendall("a string".encode())  # Python 3 中发送数据需要 encode()

import sys
sys.exit(1)  # 退出程序

import argparse
argparse.ArgumentParser(description="description")  # 创建一个命令行参数配置
<[argparse]>.add_argument()  # 添加参数
given_args = <[argparse]>.parser.args() # 将用户输入的数据进行转换，后续可赋值到其他变量
```

