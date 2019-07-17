import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
# dojo/views.py


# def mysum(request, numbers):
#     numbers=sum(map(lambda s: int(s or 0), numbers.split('/')))
#     return HttpResponse(numbers)

# def hello(request, name, age):
#     produce = '안녕하세요. %s. %s살이시네요' %(name,age)
#     return HttpResponse(produce)
#

def post_list1(request):
    name = '공유'
    return HttpResponse('''
    <h1>정성모</h1>
    <p>{name}</p>
    <p>여러분의 파이썬 </p>
    '''.format(name=name))


def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list2.html', {'name':name})

def post_list3(request):
    return JsonResponse({
        'message': '안녕 나는 장고라고해?',
        'items': ['파이썬', '장고', 'celery']
    }, json_dumps_params={'ensure_ascii': False})

def excel_download(request):
    # filepath = '\pythonPiro\Djangopractice\startproject1/gdplev.xls'
    filepath = os.path.join(settings.BASE_DIR, 'gdplev.xls') #절대경로 바로 아래있는 파일이름
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response