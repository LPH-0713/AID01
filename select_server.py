'''
基于select方法的IO多路复用网络并发
    重点代码!!
'''

from select import select
from socket import *

HOST = "0.0.0.0"
PORT = 2021
ADDR = (HOST, PORT)


def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("listen the port %d" % PORT)
    sock.setblocking(False)

    rlist = [sock]
    wlist = []
    xlist = []
    # 循环接收客户端连接
    while True:
        rs, ws, xs = select(rlist, wlist, xlist)
        # 逐个取值,分情况讨论
        for r in rs:
            if r is sock:  # 如果拿出来的r是sock类型
                connfd, addr = r.accept()  # 连接客户端
                print("Connect from", addr)
                sock.setblocking(False)

                # 将客户端套接字添加到监控列表
                rlist.append(connfd)  # 将客户端添加到select监控中
            else:
                data = r.recv(1024).decode()
                # 客户端退出
                if not data:
                    rlist.remove(r)  # 删除监控列表中已退出的客户端
                    r.close()
                    continue
                print(data)
                r.send(b"OK")


if __name__ == '__main__':
    main()
