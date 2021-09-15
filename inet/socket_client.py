# encoding=utf-8
import time
import socket
import threading

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 生成tcp服务器的套接字
tcpSerSock.bind(ADDR)  # 把套接字绑定到服务器的地址上
tcpSerSock.listen(5)  # 最多允许5个连接同时连进来，后来的连接就会被拒绝


def connectThread():
    pass


if __name__ == '__main__':
    while True:
        print('...WAITING FOR CONNECTION')
        tcpCliSock, addr = tcpSerSock.accept()
        print('CONNECTED FROM: ', addr)
        chat = threading.Thread(target=connectThread, args=(tcpCliSock, None))
        chat.start()
