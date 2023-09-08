from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound,Http404
from proc.go_ import *
from korp.forms import  *
from django.shortcuts import redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

menu=get_menu()



def index(request:HttpRequest):
    return HttpResponse('Страница корпоративного сайта')



def company (request:HttpRequest):
    title='О компании'
    page = get_pages(1)
    menuitem=1
    content=page.content
    context = {'menu': menu, 'title': title, 'content': content, 'page': page}
    return render(request=request,template_name='korp/page.html', context=context )


def projects (request:HttpRequest):
    title='Проекты'
    menuitem =6
    page = get_pages(6)
    content=page.content
    context = {'menu':menu, 'title':title, 'content': content }
    return render(request=request,template_name='korp/page.html',context=context )

#-------------------------------------------------------------------------------------------------
def events (request:HttpRequest):
    '''показывает список событий '''
    title='События'
    menuitem =3
    page = get_pages(3)
    content = page.content
    pages=Pages.objects.filter(cat_id=2)
    context={'menu': menu, 'title': title, 'content': content, 'pages': pages, 'menuitem':menuitem}
    return render(request=request,template_name='korp/events.html',context=context )



def event (request:HttpRequest, post_id:int):
    '''показывает страницу одного события '''
    page = get_pages(post_id)
    title = page.title
    context = {'menu': menu, 'title': title, 'page': page}
    return render(request=request, template_name='korp/page.html', context=context)



def postevent (request:HttpRequest):
    '''форма добавления события'''
    title = 'Форма добавления курса (для зарегистрированного клиента)'
    menuitem =4

    if request.method == "POST":
        form = addPageForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            try:
                Pages.objects.create(**form.cleaned_data)
                form.title
                content = f'КУРС  ДОБАВЛЕН'
                context = {'menu': menu, 'title': title, 'form': '', 'menuitem': menuitem, 'content': content}
                return render(request=request, template_name='korp/form_appl.html', context=context)

                #return redirect('home_ref')
            except:
                form.add_error(None, 'Ошибка добавления курса')
    else:
        form = addPageForm()
        content= ''
        context = {'menu': menu, 'title': title, 'form': form, 'menuitem': menuitem, 'content':content }
        return render(request=request, template_name='korp/form_appl.html', context=context)

#------------------------------------------------------------------------------------------------

def categs (request:HttpRequest,categ_id:int):
    return HttpResponse(f'Выбрана категория с id=  {categ_id}')


def testView (request:HttpRequest):
    if request.method=='POST':
        pass
    elif request.method=='GET':
        pass

class classTestView (LoginRequiredMixin, View):
    def post (request:HttpRequest):
        pass

    def get (request:HttpRequest):
        pass





def project (request:HttpRequest)-> HttpResponse:
    title='Проект'
    page = get_pages(6)
    menuitem =6
    content=page.content
    context = {'menu': menu, 'title': title, 'content': content, 'menuitem':menuitem}
    return render(request=request, template_name='korp/page.html', context=context)


def contacts (request:HttpRequest)-> HttpResponse:
    title='Контакты'
    page = get_pages(2)
    menuitem =2
    content=page.content
    context = {'menu': menu, 'title': title, 'content': content,'menuitem':menuitem}
    return render(request=request, template_name='korp/page.html', context=context)




def form (request:HttpRequest)-> HttpResponse:
    '''форма заявки на курс'''
    title = 'Форма заявки на курс'
    menuitem =3
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

    context = {'menu': menu, 'title': title, 'form':form, 'menuitem':menuitem}
    return render(request=request, template_name='korp/form_appl.html', context=context)







def login (request:HttpRequest):
    menuitem =5
    title = 'ЛОГИН КЛИЕНТА'
    content = "ЛОГИН КЛИЕНТА"
    context = {'menu': menu, 'title': title, 'content': content}
    raise Http404()
    return render(request=request, template_name='korp/page.html', context=context)

    #return HttpResponse('Login')



def pageNotFound (request:HttpRequest,exception):
    return HttpResponseNotFound('Страница ошибка')



# Create your views here.
