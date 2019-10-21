from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request,'index1.html')
def shebao(request):
    if request.method=='GET':
        return render(request,'index1.html')
    elif request.method=='POST':
        base = request.POST.get('base')
        try:
            base=float(base)
        except:
            error = '请检查'
            return render(request, 'index1.html',locals())
        if base<3082:
            base=3082
        elif base>23118:
            base=23118
        is_city=request.POST.get('is_city')
        if is_city=='0':
            grsy=0
            dwsy=round(base*0.008,2)
        else:
            grsy=round(base*0.002,2)
            dwsy=round(base*0.008,2)

        grylj= round(base*0.08,2)
        dwylj=round(base*0.19,2)
        dwgs=round(base*0.005,2)
        dwsy=round(base*0.008,2)
        gryylbx=round(base*0.002,2)+2
        dwylbx=round(base*0.1,2)
        grgjj=round(base*0.12,2)
        dwgjj=round(base*0.12,2)
        gs=grsy+grylj+gryylbx+grgjj
        ds=dwsy+dwylj+dwgs+dwsy+dwylbx+dwgjj
        sum=round(gs+ds,2)
        print('***',sum)
        return render(request, 'shebao.html', locals())

def test_url(request):
    # 测试url反向解析
    return render(request,'test_url.html')
def page_view(request):
    return HttpResponse('This is page html')
def pagen_view(request,n):
    html = 'This is page%s html'%n
    return HttpResponse(html)

def test_static(request):
    # 测试静态文件加载
    return render(request,'test_static.html')
