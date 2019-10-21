'''views文件需要自己创建，命名不局限于views
'''
# 函数名可以自己起
from django.http import HttpResponse

post_html = '''<form method='post' action="/page2">
    姓名:<input type="text" name="username">
    <input type='submit' value='登陆'>
</form>
'''
def index(request):
    # 获取客户端ip
    print('***',request.META['REMOTE_ADDR'])
    html = '<h1>首页</h1>'
    return HttpResponse(html)
def page1_view(request):
    # http://127.0.0.1:8000/page1？a=1111/
    print(1111)
    # print(request.GET.get('a'))
    print(2222)
    # http://127.0.0.1:8000/page1？a=1111&a=1233/ 如果有重复，.get()方法只能取最后一个以后面为准--->123321
    # print(request.GET.get('a'))
    # .getlist()方法可以通过数组把所有的值返回回来
    print(request.GET.getlist('a'))

    print(333)
    # http://127.0.0.1:8000/page1？a=1111&a=1233&b=7878/
    print(dict(request.GET))#返回一个字典，键为字符，值为查到的列表
    html = '<h1>第一个页面</h1>'
    return  HttpResponse(html+post_html)
def page2_view(request):
    if request.method=='POST':
        print(request.POST.get('username'))
    html = '<h1>第二个页面</h1>'
    return  HttpResponse(html)

def pagen_view(request,n):
    html = '--这是第%s个页面--'%n
    return HttpResponse(html)

def date_view(request,n,m):
    html = '--这是第%s个页面--'%n
    return HttpResponse(html)

def math_view(request,n1,c,n2):
    n1=int(n1)
    n2=int(n2)
    if c=='add' or c=='+':
        html = '%s+%s=%s'%(n1,n2,n1+n2)
    elif c=='sub' or c=='-':
        html = '%s-%s=%s'%(n1,n2,n1-n2)
    elif c=='mul' or c=='*':
        html = '%s*%s=%s'%(n1,n2,n1*n2)
    elif c=='/':
        html = '%s/%s=%s'%(n1,n2,n1/n2)
    else:
        html='sorry you key is wrong!!'
    return HttpResponse(html)
def person_view(request,age,name):
    html = '%s今年%s岁'%(name,age)
    return HttpResponse(html)
def birthday_view(request,year,mounth,day):
    if int(mounth)>12:
        html = '月份错误'
    elif int(day)>31 or int(mounth)==2 and int(day)>30:
        html = '天数错误'
    else:
        html = '%s年%s月%s日'%(year,mounth,day)
    return HttpResponse(html)