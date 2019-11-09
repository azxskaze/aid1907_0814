import base64
import copy
import hmac
import json
import time
class Jwt:
    def __init__(self):
        pass

    # 自定义base64方法,使用urlsafe_b64encode方法并且去除末尾的=,按照4的倍数再补回来
    @staticmethod
    def b64encode(j_s):
        return base64.urlsafe_b64encode(j_s).replace(b'=',b'')
    @staticmethod
    def b64decode(jwt_str):
        i = len(jwt_str) % 4
        if i != 0:
            return jwt_str + b'=' * (4 - i)
        return jwt_str

    @staticmethod
    def encode(payload,key,exp=300):
        # 第一部分
        header={'typ':'JWT','alg':'HS256'}
        header_json = json.dumps(header,sort_keys=True,separators=(',',':'))
        header_bs = Jwt.b64encode(header_json.encode())
        # 第二部分
        my_payload = copy.deepcopy(payload)
        my_payload['exp']= time.time()+int(exp)
        payload_json = json.dumps(my_payload,sort_keys=True,separators=(',',':'))
        payload_bs = Jwt.b64encode(payload_json.encode())

        # 第三部分
        str3 = header_bs+b'.'+payload_bs
        if isinstance(key,str):
            key = key.encode()


        h = hmac.new(key,str3,digestmod='SHA256')
        sign = h.digest()

        return str3+b'.'+Jwt.b64encode(sign)



    @staticmethod
    def decode(jwt_s,key):
        jwt_l=jwt_s.split(b'.')

        jwt_h=jwt_l[0]
        jwt_p=jwt_l[1]
        jwt_s=jwt_l[2]
        if isinstance(key,str):
            key = key.encode()
        str3 = jwt_h+b'.'+jwt_p

        h = hmac.new(key,str3,digestmod='SHA256')
        if Jwt.b64encode(h.digest()) != jwt_l[2]:
            print(base64.urlsafe_b64encode(h.digest()),jwt_s)
            raise Exception('error1')

        json_p = base64.urlsafe_b64decode(Jwt.b64decode(jwt_p))
        str_p = json.loads(json_p.decode())
        if str_p['exp']<=time.time():
            raise Exception('error2')
        return str_p






if __name__ == '__main__':

    a=Jwt.encode({'username':'chen'},'dsada',1.8)
    time.sleep(1.9)
    print(Jwt.decode(a,'dsada'))


