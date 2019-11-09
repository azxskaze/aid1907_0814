'''微博共同关注'''
import redis

r = redis.Redis(host='176.234.6.27', port='6379', db=0, password='123456')
r.sadd('set_a','saber','lancer','berserker','rider','archer')
r.sadd('set_b','saber','shiki','umr')

# 共同关注
foucs = r.sinter('set_a','set_b')
print('共同关注',foucs)