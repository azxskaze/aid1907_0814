from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('176.234.6.35',1234))
s.listen(5)
while True:
    '''文件打开关闭语句都应该写到循环里面
    才能实现网页循环获取内容'''
    f = open('index.html', 'r')
    c,addr = s.accept()
    print('',addr)
    data = c.recv(4096).decode()
    print(data)
    print(data.split('\n')[0].split(' ')[1][0])
    if data.split('\n')[0].split(' ')[1] =='/':
        '''如果GET 后面的请求是‘/’ 就发送文件'''
        html1 = '''HTTP/1.1 200 OK
        Content-Type:text/html

        %s
        '''%f.read(1024)
        f.close()
    else:
        html1 = '''HTTP/1.1 200 OK
        Content-Type:text/html

        <h1>sorry</h1>
        '''
    c.send(html1.encode())
    c.close()
