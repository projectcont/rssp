from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect

from excelsite.settings import deploy
from korp.forms import *
from utils.context_items_ import context_items
from utils.get_by_id import *


def index(request: HttpRequest):
    return HttpResponse('Страница корпоративного сайта')


#  --- представление типовой страницы  -------------------------------------------------------------------------------------------------
def page(request: HttpRequest, pagetitle='неопр', menuitem=0) -> HttpResponse:
    if ((menuitem == 1001) or (menuitem == 300)):
        page = get_page_by_id(1)
    elif menuitem == 1002:
        page = get_page_by_id(2)
    else:
        page = get_page_by_id(2)

    if page.metatitle:
        metatitle = page.metatitle
    else:
        metatitle = page.title

    if page.metadescription:
        metadescription = page.metadescription
    else:
        metadescription = page.title

    title = page.title

    content = page.content
    context = {'metatitle': metatitle, 'metadescription': metadescription, 'title': title, 'content': content,
               'page': page, 'menuitem': menuitem, 'deploy': deploy}
    return render(request=request, template_name='page.html', context=context)


#  --- представление списка объектов  -------------------------------------------------------------------------------------------------

def items(request: HttpRequest, menu_id=0) -> HttpResponse:
    ''' показывает список объектов '''

    context = context_items(menu_id)
    items = context['items']

    filter_data = {'filter_okrug': '', 'square_from': '', 'square_to': '', }
    if 'filter_applied' in request.GET:
        import utils.filter_realty
        items = utils.filter_realty.go(request.GET, filter_data, items)
        # print(len(zavs))

    context['items'] = items
    context.update(filter_data)
    print("context=", context)

    return render(request=request, template_name='realty/category.html', context=context)


#  ----------- представление страницы одного объекта  ----------------------------------------

def Item(request, pk, categ):
    ''' показывает страницу выбранного объекта '''

    print('categ=', categ)

    if True:
        if categ == "ofis": item = Ofis.objects.get(pk=pk)
        if categ == "torg": item = Torg.objects.get(pk=pk)
        if categ == "tc": item = Tc.objects.get(pk=pk)
        if categ == "proizv": item = Proizv.objects.get(pk=pk)
        if categ == "sklad": item = Sklad.objects.get(pk=pk)
        if categ == "psn": item = Psn.objects.get(pk=pk)
        if categ == "land": item = Land.objects.get(pk=pk)
        if categ == "flat": item = Flat.objects.get(pk=pk)

        try:
            itemfields = item.get_fields()
        except Exception:
            raise

        exclude = ['id', 'title', 'time_create', 'worker', 'owner', 'sale', 'price_sale', 'sale_right', 'rent ',
                   'price_rent',
                   'adres', 'map', 'square', 'photo', 'rent', 'is_published',
                   'photo1', 'photo2', 'photo3', 'photo4', 'photo5', 'photo6', 'photo7', 'photo8', 'photo9', 'photo10',
                   'maplink', 'categ', 'idl', 'description', 'export_avito', 'export_yandex', 'export_afi',
                   'export_domclik', 'export_5', 'export_6',
                   'metatitle', 'metadescription', 'okrug', 'scan', 'retail', 'rent_type', 'sale_type', '', ]

        form = ContactForm()
        context = {"item": item, "itemfields": itemfields, "exclude": exclude, 'form': form}
        return render(request=request, template_name='realty/item.html', context=context)
    else:
        return HttpResponseNotFound('Страница ошибка')


#  ----------------------------------------------------------------------------------------------------

def search(request: HttpRequest, menu_id=0) -> HttpResponse:
    ''' показывает поиск объектов '''
    return HttpResponse('<h1 style="margin:20px auto; text-align:center">В СТАДИИ РАЗРАБОТКИ</h1>')


# --- отправка формы------
def formsent(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Пробное сообщение"
            print(subject, form.cleaned_data['client'], form.cleaned_data['phone'])
            body = {
                'client': form.cleaned_data['client'],
                'phone': form.cleaned_data['phone'],
            }
            message = "\n".join(body.values())
            try:

                import imaplib
                import ssl
                ctx = ssl.create_default_context()
                ctx.set_ciphers('DEFAULT')
                imapSrc = imaplib.IMAP4_SSL('mail.safemail.it', ssl_context=ctx)

                send_mail(subject, message,
                          'admin@example.com',
                          ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("main:homepage")

    form = ContactForm()
    return render(request, "formsent.html", {'form': form})


def pageNotFound(request: HttpRequest, exception):
    return HttpResponseNotFound('Страница ошибка')
