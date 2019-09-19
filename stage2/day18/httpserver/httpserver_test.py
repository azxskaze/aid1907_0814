from socket import *
import json
from config import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind((frame_ip,frame_port))
s.listen(5)

c,addr = s.accept()
data = c.recv(4096)
print(data.decode())
c.send(json.dumps({'status':'200','data':'ccc'}).encode())
c.close()
s.close()
