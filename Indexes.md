# Python 网络编程攻略

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

## 1.6 主机字节序和网络字节序之间相互转换
- 编写底层网络应用时，有时需要处理通过电缆在两台设备之间传送的底层数据。需要把主机操作系统发出的数据转换成网络格式或逆向转换
- 所用函数

```py
from socket
socket.ntohl(data) # 网络字节序 -> 长整形主机字节序
socket.htonl(data) # 主机字节序 -> 长整形网络字节序

socket.ntohs(data) # 网络字节序 -> 短整形主机字节序
socket.htons(data) # 主机字节序 -> 短整形网络字节序
```
## 1.7 设定并获取默认的套接字超时时间
- 获取或设置套接字超时时间
- 所用函数

```py
from socket
socket.socket(socket.AFINET, socekt.SOCK_STREAM) # 创建一个基于 TCP 协议，IP 地址为 IPv4 类型的套接字对象

# <[Class]> 表示 Class 对象的一个实例
<[socket]>.gettimeout() # 获取超时时间，默认为 None
<[socekt]>.settimeout(<timeout>) # 设置超时时间
```

## 1.8 处理 socket 错误
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

## 1.9 修改 socket 发送和接收缓冲区大小
- 所用方法

```py
import socket

# 参数分别为：常量符号（需要查），选项名称，值
sock.getsockopt(<level>, <option name>)
sock.setsockopt(<level>, <option name>, value)
```
## 1.10 将 socket 改成阻塞式或非阻塞式
- 所用方法

```py
import socket

# 设置是否为阻塞式。True 为阻塞，False 为非阻塞
<[socket]>.setblocking(<flag>)

# 上述方法等同于调用
<[socket]>.settimeout(None) # True
<[socket]>.settimeout(0.0) # False

# 绑定 socket，当端口为0时，系统自动从 1024~65535 之间选择可用的端口
<[socket]>.bind(<IP:port as a tuple>)

# 获取 socket 地址，特别是自动获取端口的时候有用
<[socket]>.getsockname()

# 监听，参数为在拒绝新连接前可接受的连接数
<[socket]>.listen(<available connections>)
```

# 1.11 重用 socket 地址
- 在某个端口上运行一个 Python socket 服务器，连接一次后终止运行，就不能再使用该端口，否则抛异常。为此，需要设置端口可重用来解决该问题
- 所用方法

```py
import socket

# 获取 socket 地址的旧状态
[<socket>].getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDER)

# 设置 socket 地址可重用，其中的参数含义，需要以后深造
[<socket>].setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
```

- 原理
	1. 此脚本为服务端脚本，运行脚本
	- 利用 `telnet localhost 8282(脚本中定义的端口)` 连接到服务端
	- 使用 `Ctrl-C` 终止服务端运行，再重启服务端，接下来的事就有趣了 
	- 分情况
		1. 服务端 **没有** 设置 socket 地址可重用，抛出异常，因为旧端口还没有释放
		2. 服务端 **有** 设置 socket 地址可重用，正常启动

# 1.12 从网络时间服务器获取当前时间
- 本地机器的时间可能不准确，从网络时间服务器获取更可靠
- 原理
	- 使用 ntplib，通过网络时间协议 Network Time Protocol a.k.a NTP 处理客户端和服务器之间的通信
	- 需通过 pip 等工具安装 ntplib

- 所用方法

```py
import ntplib
# 创建一个 NTP 客户端
ntp_client = ntplib.NTPClient()

# 向 NTP 服务器发送请求并获得一个结果
response = ntp_client.request("pool.ntp.org")

from time import ctime
# 转换时间
ctime(<以秒表示的时间>)
```


