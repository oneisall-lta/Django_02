import datetime

from django.shortcuts import render


def show_fruit(request):
    fruits = ['苹果', '香蕉', '榴莲', '菠萝蜜']
    return render(request, 'fruit.html', {'fruits': fruits})


# def show_sports(req):
#     url = req.path
#     print(url)
#     return render(req,'sports.html',{'url': url})
def show_sports(req, tag):
    list = []
    if tag == 'allsports':
        list = ['排球', '足球', '网球']
    return render(req, 'sports.html', {'list': list})


def welcome(req):
    # if req.method == 'GET':
    #     return render(req,'welcome.html')

    username = req.POST.get('username')
    pwd = req.POST.get('pwd')
    sex = req.POST.get('sex')
    return render(req, 'welcome.html', {'username': username, 'pwd': pwd, 'sex': sex})


def register(request):
    return render(request, 'register.html')


def trans_date(request):
    cur_date = datetime.datetime.now()
    print(cur_date)
    return render(request, 'date.html', {'cur_time': cur_date})
