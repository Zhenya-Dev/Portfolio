from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import *

menu=[{'title': "Про сайт", 'url_name':'about'},
      {'title':"Додати статтю", 'url_name': 'add_page'},
      {'title':"Зворотній зв'язок", 'url_name':'contact'},
      {'title':"Увійти", 'url_name': 'login'}
]

# def index(request):
#     return HttpResponse("Сторінка додатку Ukraine")
def index(request):
    posts = Ukraine.objects.all()
    context={
        'posts':posts,
        'menu':menu,
        'title':'Головна сторінка',
        'cat_selected': 0,
    }
    return render(request, 'ukraine/index.html', context=context)

def about(request):
    return render(request, 'ukraine/about.html', {'menu': menu,'title':' Про сайт'})

# def categories(request, catid):
#     # if (request.GET):
#     #     print(request.GET)
#     if (request.POST):
#         print(request.POST)
#     return HttpResponse(f"<h1>Статті по категоріях</h1><p>{catid}</p>")
#
# def archive(request, year):
#     if int(year)>2020:
#         # return redirect('/', permanent=True)
#         return redirect('home', permanent=True)
#     return HttpResponse(f"<h1>Архів за роками</h1><p>{year}</p>")

# def show_post(request, post_id):
#     return HttpResponse(f'Стаття {post_id}')

def show_post(request, post_slug):
    post = get_object_or_404(Ukraine, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id
    }

    return render(request, 'ukraine/post.html', context=context)


def addpage(request):
    return HttpResponse('Додавання статті')

def contact(request):
    return HttpResponse("Звортній зв`язок")

def login(request):
    return HttpResponse("Авторизація")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')

def show_category(request, category_slug):
    posts = Ukraine.objects.filter(cat__slug=category_slug)
    print(posts)
    context = {
        'posts' : posts,
        'menu' : menu,
        'title' : 'Відображення по рубриках',
        'cat_selected': posts[0].slug,
    }

    return render(request, 'ukraine/index.html', context=context)


