from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotModified, HttpResponseBadRequest, \
    HttpResponseForbidden, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponseGone, HttpResponseServerError, \
    JsonResponse
from django.shortcuts import render



def index(request):
    BMW = Cars('BMW','X5',1995)
    return JsonResponse(BMW, safe=False, encoder=CarsEncoder)
class Cars:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
class CarsEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Cars):
            return {'brand':obj.brand, 'model':obj.model, 'year':obj.year}
        return super().default(obj)

def user_info(request, f_name='', l_name='', age=0):
    Users = User(f_name, l_name, age)
    return JsonResponse(Users, safe=False, encoder=UserEncoder)

class User:
    def __init__(self, f_name, l_name, age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
class UserEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return{'f_name':obj.f_name, 'l_name':obj.l_name, 'age':obj.age}
        return super().default(obj)



def homedef(request):
    return HttpResponse('<h1>Home page</h1>')

def about(request):
    return HttpResponseRedirect('/')

def info(request):
    return HttpResponseRedirect('/person?name=Aleks') #по левую сторону от знака ? указан путь, по правую атрибуты где имя будет алекс а возраст из умолчания функции Персон

def cardef(request, brand='', model='', year=''):
    if brand:
        brand = f'<h3>brand:{brand}</h3>'
    if model:
        model = f'<h2>model:{model}</h2>'
    if year:
        year = f'<h1>year:{year}</h1>'
    return HttpResponse(f'{brand}{model}{year}')

def person(request):
    age = request.GET.get('age', 99)
    name = request.GET.get('name','John') #второе значение задается по умолчанию
    return HttpResponse(f'{age}{name}')

def error(request):
    return HttpResponseNotModified('update_info')    # 304
    # return HttpResponseBadRequest()     # 400 не правильный синтаксис/запрос
    # return HttpResponseForbidden()      # 403 запрещенная стр
    # return HttpResponseNotFound()       # 404 нет данных
    # return HttpResponseNotAllowed()     # 405 http request was changed
    # return HttpResponseGone()           # 410 early page was here, but she was deleted
    # return HttpResponseServerError()    # 500
# Create your views here.

