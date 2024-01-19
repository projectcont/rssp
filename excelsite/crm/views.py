from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
import utils.get_okrug_titles
import utils.get_okrug_ids
import utils.get_filter
from korp.models import Realty

import utils.fotos_amount  as     fotos_amount
import utils.fotos_media_paths as fotos_media_paths
import utils.fotos_copy as fotos_copy
import utils.fotos_format1  as fotos_format1
import utils.fotos_format2 as fotos_format2
import utils.fotos_orig as fotos_orig
import utils.check as check_


from .models import *


def requests (request: HttpRequest, menuitem=0) -> HttpResponse:
    ''' показывает список заявок '''
    if True:
    #if request.user.is_authenticated:
        items = Zayavki.objects.all()
        context = {'items': items, 'user':request.user, 'menuitem':menuitem, 'sotr': True, }
        return render(request=request, template_name='sotrud/requests.html', context=context)
    else:
        return HttpResponse("нет доступа")


#---------------------------------------------------------------------------------

def itemreq (request: HttpRequest, id: int, menuitem=0) -> HttpResponse:
    print(request.user.is_authenticated)

    ''' показывает страницу заявки со списком подходящих объктов'''

    print("menuitem", menuitem)

    #if request.user.is_authenticated:
    if True:
        item = Zayavki.objects.get(pk=id)
        okrug_str_titles = utils.get_okrug_titles.go(item)
        okrug_list_ids = utils.get_okrug_ids.go(item)
        rentsale=item.rentsale
        if rentsale == "rent": pricetype = "руб./месяц";
        if rentsale == "sale": pricetype = "руб.";
        square=item.square
        price=item.price
        categ = item.categ
        #menu_id=get_menuid_categ(categ)

        # фильтрация списка
        realty_items_selected = utils.get_filter.go(price=price, square=square, okrug_list=okrug_list_ids, categ=categ, rentsale=rentsale)

        if len(realty_items_selected)>0:
            result = 'Список объектов по этой заявке'
        else:
            result = 'Нет объектов по данной заявке'

        context={ 'pricetype': pricetype,   'rentsale':rentsale,   'item': item, 'result':result, 'menuitem':menuitem, "realties" : realty_items_selected, 'okrug_str_titles': okrug_str_titles, 'sotr': True }
        return render(request=request, template_name='sotrud/podbor.html', context=context)
    else:
        return HttpResponse("нет доступа")


#---------------------------------------------------------------------------------

def formatfotos (request: HttpRequest,  menuitem=0) -> HttpResponse:

    media_paths = fotos_media_paths.go()
    photos_number = fotos_amount.go(media_paths)
    result=''

    if  'fotoformat1' in request.GET:
        width_to = request.GET.get('fotoformat1')
        fotos_copy.go(media_paths)
        result = fotos_format1.go(media_paths,width_to)
    else:
        pass

    if 'fotoformat2' in request.GET:
        width_to = request.GET.get('fotoformat2')
        height_to = request.GET.get('fotoformat3')
        fotos_copy.go(media_paths)
        result = fotos_format2.go(media_paths, width_to, height_to)
    else:
        pass
    if 'from_orig' in request.GET:
        result=fotos_orig.go(media_paths)
    else:
        pass

    context = {  'menuitem':menuitem, 'photos_number': photos_number , "result": result }
    return render(request=request, template_name='sotrud/formatfotos.html', context=context)


#------ check ---------------------------------------------------------------------------
def check (request: HttpRequest, menuitem=0) -> HttpResponse:
    if True:
    #if request.user.is_authenticated:
        result=''

        if  'check' in request.GET:
            result = check_.go()
        context = { 'sotr': True, 'menuitem': menuitem, "result" : result}
        return render(request=request, template_name='sotrud/check.html', context=context)

    else:
        return HttpResponse("нет доступа")







#-----  avito  ----------------------------------------------------------------------------

def avito (request: HttpRequest, menuitem=0) -> HttpResponse:
    ''' показывает настройки экспорта avito '''
    if True:
    #if request.user.is_authenticated:
        item = Export.objects.get(pk=1)

        if item.is_using : is_using = 1
        else:  is_using = 0

        if  'avito_off' in request.GET:
            item.is_using = False
            item.title = "Avito"
            item.save()

        if  'avito_on' in request.GET:
            item.is_using = True
            item.title = "Avito"
            item.save()

        if  'export_update' in request.GET:
            import export.avito_update
            items = Realty.objects.filter(is_published=True, export_avito=True)
            export.avito_update.go(items)


        context = {'is_using': is_using, 'sotr': True, 'menuitem': menuitem}
        return render(request=request, template_name='sotrud/avito.html', context=context)

    else:
        return HttpResponse("нет доступа")




