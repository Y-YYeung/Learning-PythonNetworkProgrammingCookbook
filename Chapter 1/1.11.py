# 重用套接字地址

import socket
import sys

def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取旧的 socket 地址状态
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Old sock state: %s" % old_state)

    # 设置 socket 地址可重用
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("New sock state: %s" % new_state)

    # 以上的代码应该只是用来演示 [<socket>].setsockopt 的效果。。。
    # 下面才是我们的本例子真正工作的部分

    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 这一行是重点
    srv.bind(('', local_port))
    srv.listen(1)
    print("Listening on port: %s " % local_port)
    while True:
        try:
            connection, addr = srv.accept()
            print("Connected by %s:%s" % (addr[0], addr[1]))
        except KeyboardInterrupt:
            # 捕捉 Ctrl-C 动作，终止运行而不会显示异常消息
            break
        except socket.error as msg:
            print("%s" % (msg,))

if __name__ == "__main__":
    reuse_socket_addr()
