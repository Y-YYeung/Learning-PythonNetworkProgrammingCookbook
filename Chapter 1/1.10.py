# 将 socket 改成阻塞式或非阻塞式

# 非阻塞式，send() / recv() 遇到问题会抛出异常
# 阻塞式，遇到错误不会阻止操作

import socket

def test_socket_modes():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket 设置为阻塞式
    s.setblocking(True)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))

    socket_address = s.getsockname()
    print("Trivial server launched on socket: %s" % str(socket_address))
    while 1:
        s.listen(1)

if __name__ == "__main__":
    test_socket_modes()