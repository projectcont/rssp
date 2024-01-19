from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from proc.get_by_id import *
from excelsite.settings import deploy
from django.views.generic import ListView, DetailView, CreateView
from korp.forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.urls import reverse_lazy


def index(request: HttpRequest):
    return HttpResponse('Страница корпоративного сайта')

#  --- представление типовой страницы  -------------------------------------------------------------------------------------------------
def page (request: HttpRequest, pagetitle='неопр', menuitem=0) -> HttpResponse:
    if ((menuitem == 1001) or (menuitem == 300)) :
        page = get_page_by_id(1)
    elif menuitem == 1002:
        page = get_page_by_id(2)
    else:
        page = get_page_by_id(2)

    if page.metatitle:
        metatitle=page.metatitle
    else:
        metatitle=page.title

    if  page.metadescription:
        metadescription=page.metadescription
    else:
        metadescription = page.title

    title = page.title

    content = page.content
    context = {'metatitle': metatitle, 'metadescription': metadescription,  'title': title, 'content': content, 'page': page, 'menuitem': menuitem, 'deploy': deploy}
    return render(request=request, template_name='page.html', context=context)


#  --- представление списка объектов и страницы одного события -------------------------------------------------------------------------------------------------

def items (request: HttpRequest,menu_id=0) -> HttpResponse:
    ''' показывает список объектов '''
    from proc.context_items_ import  context_items
    context=context_items(menu_id)
    return render(request=request, template_name='realty/category.html', context=context)



def Item (request, pk, categ):
    ''' показывает страницу выбранного объекта '''

    print('categ=', categ)

    if  True:
        if categ == "ofis": item = Ofis.objects.get(pk=pk)
        if categ == "torg" : item = Torg.objects.get(pk=pk)
        if categ == "tc": item = Tc.objects.get(pk=pk)
        if categ == "proizv": item = Proizv.objects.get(pk=pk)
        if categ == "sklad": item = Sklad.objects.get(pk=pk)
        if categ == "psn": item = Psn.objects.get(pk=pk)
        if categ == "retail": item = Retail.objects.get(pk=pk)
        if categ == "land": item = Land.objects.get(pk=pk)
        if categ == "flat": item = Flat.objects.get(pk=pk)

        try:
            itemfields= item.get_fields()
        except Exception:
            raise

        exclude=['id', 'title', 'time_create',  'worker',  'owner',  'sale',  'price_sale',  'sale_type',  'sale_right',  'rent ',  'price_rent',
                 'adres',  'map', 'square', 'photo', 'rent', 'rent_type', 'is_published',
                 'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7','photo8','photo9','photo10',
                 'maplink',  'categ',  'idl',  'description',  'export_avito',  'export_yandex',  'export_afi',  'export_domclik',  'export_5',  'export_6',
                 'metatitle',   'metadescription',   'okrug',   '',   '',   '',   '',   '',    ]

        context={ "item": item,   "itemfields":itemfields, "exclude": exclude }
        return render(request=request, template_name='realty/item.html', context=context)
    else:
        return HttpResponseNotFound('Страница ошибка')

#  ----------------------------------------------------------------------------------------------------


def search (request: HttpRequest,menu_id=0) -> HttpResponse:
    ''' показывает поиск объектов '''
    #return render(request=request, template_name='category.html', context=context)
    return HttpResponse('<h1 style="margin:20px auto; text-align:center">В СТАДИИ РАЗРАБОТКИ</h1>')


class LoginUser (LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Логин пользователя'
        return context

'''
def font(request: HttpRequest, pagetitle='неопр', menuitem=0) -> HttpResponse:
    page = get_page_by_id(1)
    content = page.content
    context = {'title': pagetitle, 'content': content, 'page': page, 'menuitem': menuitem}
    return render(request=request, template_name='page.html', context=context)
 
class PostItem (LoginRequiredMixin, CreateView):
    form_class = addPageForm
    template_name = 'post_event.html'
    success_url = reverse_lazy('home_ref')
    login_url =  reverse_lazy('home_ref')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Добавление страницы'
        print("context====", context)
        return context

def categs(request: HttpRequest, categ_id: int):
    return HttpResponse(f'Выбрана категория с id=  {categ_id}')
'''


def pageNotFound(request: HttpRequest, exception):
    return HttpResponseNotFound('Страница ошибка')
