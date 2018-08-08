from django.shortcuts import render

# Create your views here.
from templateapp.person import Person


def dict_info(req):  # 给模板传递字典
    info = {'name': 'tom', 'age': 20, 'sex': 'male'}
    return render(req, 'myTemplate/demo.html', {'dict': info})


def obj_info(req):  # 给模板传递对象
    per = Person('John', 20, 'male')
    return render(req, 'myTemplate/demo.html', {'people': per})


def list_info(req):
    fruits = ['苹果', '香蕉', '榴莲', '菠萝蜜']
    return render(req, 'myTemplate/demo.html', {'list': fruits})


def iftag(req):
    athletes = ['内马尔', 'C罗', '梅西']
    coachs = ['cici', 'didi', 'eiei']
    return render(req, 'myTemplate/iftags.html', {'athletes': athletes, 'coachs': coachs})


def books_info(req):
    books = ['呼啸山庄', '西游记', '西厢记']
    links = ['百度', '小米', '谷歌']
    fruits = []
    return render(req, 'myTemplate/fortag.html', {'book_list': books, 'link': links, 'fruits': fruits})
