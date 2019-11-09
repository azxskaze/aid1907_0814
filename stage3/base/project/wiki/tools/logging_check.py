import jwt
from django.http import JsonResponse
from user.models import User

TOKEN_KEY='woshimima'
def logging_check(*method):
    def _login_check(func):
        def wrapper(request,*args,**kwargs):
            if not method:
                return func(request,*args,**kwargs)
            else:
                if request.method not in method:
                    return func(request, *args, **kwargs)
            # 取出token
            token = request.META.get('HTTP_AUTHORIZATION')
            if not token:
                result = {'code':20104,'error':'login'}
                return JsonResponse(result)
            try:
                res = jwt.decode(token,TOKEN_KEY,algorithms='HS256')
            except:
                result={'code':20105,'error':'login'}
                return JsonResponse(result)
            login_time = res.get('login_time')

            username = res['username']
            user = User.objects.get(username=username)
            if login_time != str(user.login_time):
                result = {'code': 20106, 'error': 'some one is login'}
                return JsonResponse(result)
            request.user=user
            return func(request,*args,**kwargs)

        return wrapper
    return _login_check



def get_user_by_request(request):
    """
尝试获取用户身份
    :param request:
    """
    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return None
    try:
        res = jwt.decode(token, TOKEN_KEY, algorithms='HS256')
    except:
        return None
    username = res['username']
    users = User.objects.filter(username=username)
    if not users:
        return None
    return users[0]