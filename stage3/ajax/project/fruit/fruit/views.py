from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
import hashlib

from index.models import User


def login(request):
    if request.method=='GET':
        # return HttpResponseRedirect('/index/index')

        return render(request,'login.html')
    elif request.method=='POST':
        save_cookie=False
        if 'save_cookie' in request.POST.keys():
            save_cookie = True
        uname = request.POST.get('username')
        upwd = request.POST.get('userpass')
        print(upwd,uname)

        try:
            user = User.objects.get(uname=uname,upwd=upwd)
        except:

            print('***********')
            return render(request,'login.html')
        resp = HttpResponseRedirect('/index/index')
        if save_cookie:
            resp.set_cookie('username1', uname, 60 * 60 * 24 * 30)
            resp.set_cookie('uid1', user.id, 60 * 60 * 24 * 30)
        return resp


def logon(request):
    return render(request,'logon.html')


def phone(request):
    uphone = request.GET.get('phone')
    user = User.objects.filter(uphone=uphone)
    if user:
        return JsonResponse({'i': False})
    return JsonResponse({'i':True})


def register(request):
    if request.method=='POST':
        uphone = request.POST.get('uphone')
        uname = request.POST.get('username')
        if not uname:
            return render(request,'logon.html')
        uemail = request.POST.get('uemail')
        if not uemail:
            return render(request,'logon.html')
        upassword = request.POST.get('userpass')
        upassword2 = request.POST.get('userpass2')
        if not upassword:
            return render(request,'logon.html')
        if upassword != upassword2:
            return render(request,'logon.html')
        m = hashlib.md5()
        try:
            pass1 = upassword.encode()
            m.update(pass1)
        except:
            return render(request,'logon.html')
        user = User.objects.create(uphone=uphone,upwd=pass1,uname=uname,uemail=uemail)
        request.session['username1']=uname
        request.session['uid1']=user.id

        return HttpResponseRedirect('/login')
    return render(request,'logon.html')


