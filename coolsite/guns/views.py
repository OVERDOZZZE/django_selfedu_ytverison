from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Guns, Category
from django.shortcuts import get_object_or_404
# Create your views here.

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью ', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'}
]

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def index(request):
    posts = Guns.objects.all()
    cats = Category.objects.all()
    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        "cat_selected": 0,
    }

    return render(request, 'guns/index.html', context=context)


def about(request):
    return HttpResponse('О нас')


def addpage(request):
    return HttpResponse('Добавить статью')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_slug):
    post = get_object_or_404(Guns, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        "cat_selected": post.cat_id,
    }

    return render(request, 'guns/post.html', context=context)


def show_category(request, cat_id):
    posts = Guns.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(cats) == 0:
        raise pageNotFound()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        "cat_selected": cat_id,
    }

    return render(request, 'guns/index.html', context=context)


