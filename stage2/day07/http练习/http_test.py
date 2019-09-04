from socket import *
f = open('index.html','r')
s = socket()
# 创建tcp套接字
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#端口立即解除占用
s.bind(('176.234.6.35',1234))
s.listen(5)
c,addr = s.accept()
print('',addr)
data = c.recv(4096).decode()
print(data)
html1 = '''HTTP/1.1 200 OK
Content-Type:text/html

<h1>sorry111</h1>
'''

# print(html1)
c.send(html1.encode())
c.close()
s.close()