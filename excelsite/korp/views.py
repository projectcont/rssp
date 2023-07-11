from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound,Http404
from proc.go_ import *
from korp.forms import  *
from django.shortcuts import redirect

menu=get_menu()

def index(request):
    return HttpResponse('Страница корпоративного сайта')


def company (request):
    title='О компании'
    page = get_pages(1)
    content=page.content
    print('comp content=',content)
    return render(request,'korp/page.html',{'menu':menu, 'title':title, 'content': content } )


def projects (request):
    title='Проекты'
    page = get_pages(6)
    content=page.content
    return render(request,'korp/page.html',{'menu':menu, 'title':title, 'content': content } )


def kurses (request):
    title='Курсы'
    page = get_pages(3)
    content = page.content
    pages=Pages.objects.filter(cat_id=2)
    context={'menu': menu, 'title': title, 'content': content, 'pages': pages}
    return render(request,'korp/kurses.html',context=context )

def kurs (request, post_id):
    page = get_pages(post_id)
    title = page.title
    content = page.content
    context = {'menu': menu, 'title': title, 'content': content}
    return render(request, 'korp/page.html', context=context)


def categs (request,categ_id):
    return HttpResponse(f'Выбрана категория с id=  {categ_id}')


def project (request):
    title='Проект'
    page = get_pages(6)
    content=page.content
    context = {'menu': menu, 'title': title, 'content': content}
    return render(request, 'korp/page.html', context=context)


def contacts (request):
    title='Контакты'
    page = get_pages(2)
    content=page.content
    context = {'menu': menu, 'title': title, 'content': content}
    return render(request, 'korp/page.html', context=context)

def form (request):


    title = 'Форма заявки на курс'
    if request.method=="POST":
        form=addApplForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                Application.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None,'Ошибка добавления клиента')
    else:
        form = addApplForm()

    context = {'menu': menu, 'title': title, 'form':form}
    return render(request, 'korp/form_appl.html', context=context)

def postkurs (request):
    title = 'Форма добавления курса (для зарегистрированного клиента)'
    page = get_pages(4)
    content = page.content
    context = {'menu': menu, 'title': title, 'content': content}
    return render(request, 'korp/page.html', context=context)


def login (request):
    title = 'ЛОГИН КЛИЕНТА'
    content = "ЛОГИН КЛИЕНТА"
    context = {'menu': menu, 'title': title, 'content': content}
    raise Http404()
    return render(request, 'korp/page.html', context=context)

    #return HttpResponse('Login')



def pageNotFound (request,exception):
    return HttpResponseNotFound('Страница ошибка')



# Create your views here.
