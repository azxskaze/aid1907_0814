from django.http import HttpResponse

# 这个模块可以加载html页面
from django.template import loader

# shortcuts封装了一些新方法，可以代替request.method等方法，使用更加简单
from django.shortcuts import render
def index1(request):

    # 1通过loader加载模板
    t = loader.get_template('index.html')

    # 2将t对象转换成html字符串
    html = t.render()

    # 3将html return 至浏览器
    return HttpResponse(html)

    # return HttpResponse('this is index')

def index(request):
    # 传递的参数，函数，方法必须遵循模板规则
    dic = {'username':'chole','age':19}

    # 等于上面的三句话
    # 相当于将dic中的变量传参给index.html页面

    return render(request,'index.html',dic)
def test_p(request):
    # 测试传参

    dic={}
    # lst=['威娜','赛多']
    dic['lst'] = ['威娜','赛多','liya']
    dic['dict'] ={'username':'chole','age':19}
    dic['class_obj'] = Dog()
    dic['say_hi'] = say_hi
    dic['script'] ='<script>alert(111)</script>'
    dic['number'] = 1
    dic['text'] = '如果这些代码包含特殊符号而且是安全的可以才能使用此转义（防止xss攻击）'
    return render(request,'test_p.html',dic)

# 测试类
class Dog:
    def say(self):
        return '汪！'
# 测试函数
def say_hi():
    return 'say hi'

def test_if(request):
    # test_id?x=1
    x = int(request.GET.get('x',0))
    dic={'x':x}
    return render(request,'test_if.html',dic)

def math4(request):
    if request.method=='GET':
        return render(request, 'math4.html')
    elif request.method=='POST':
       # 浏览器会用POST请求提交如下数据
       # x=x_val&op=op_val&y=y_val
       # 处理数据
       # text框 空提交的时候浏览器hUI带上具体的text框的name及空值一并提价破到服务器

        x = request.POST.get('x')
        if not x:
            # 错误处理 将提示信心返回给浏览器
            error = 'no x'
            dic = {'error':error}
            return render(request,'math4.html',dic)
        try:
            x = int(x)
        except Exception as e:
            print('----%s is erro----'%x)
            try:
                x=int(float(x))
            except Exception as f:
                error = 'x is must number'
                dic = {'error':error}
                return render(request,'math4.html',dic)
        y= request.POST.get('y')
        if not y:
            # 错误处理 将提示信心返回给浏览器
            error = 'no y'
            dic = {'error': error}
            return render(request, 'math4.html', dic)
        try:
            y = int(y)
        except Exception as e:
            print('----%s is erro----' % y)
            try:
                y = int(float(y))
            except Exception as f:
                error = 'y is must number'
                dic = {'error': error}
                return render(request, 'math4.html', dic)
        op = request.POST.get('op')
        z = 99999
        if op=='add':
            z=  x+y
        elif op =='sub':
            z = x-y
        elif op =='mul':
            z = x*y
        elif op =='div':
            if y==0:
                error = 'y is not 0'
                dic = {'error': error}
                return render(request, 'math4.html', dic)
            z = x/y
        else:
            z=None

        # locals()可以将当前页面的局部变量打包成kv字典
        return render(request,'math4.html',locals())
def test_for(request):
    lst = ['红','蓝','小绿']
    dic = {'username':'ming','age':18}
    return render(request,'test_for.html',locals())

def base(request):
    lst = ['aa','bb']
    return render(request,'base.html',locals())
def sports(request):
    return render(request,'sports.html')
def music(request):
    return render(request,'music.html')
