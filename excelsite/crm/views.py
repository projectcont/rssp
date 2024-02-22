from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
import utils.get_okrug_titles
import utils.get_okrug_ids
from korp.models import *
from utils.scan_lenths import go as lenths

import utils.fotos_amount  as     fotos_amount
import utils.fotos_media_paths as fotos_media_paths
import utils.fotos_copy as fotos_copy
import utils.fotos_format1  as fotos_format1
import utils.fotos_format2 as fotos_format2
import utils.fotos_orig as fotos_orig
from utils.Realtyitem_by_id_categ_ import Realtyitem_by_id_categ
from django.contrib.auth.decorators import login_required
import utils.check


from utils.scan_color import color_
from utils.scan_select import select


from .models import *


#-------------  список заявок  --------------------------------------------------------------------
@login_required
def requests (request: HttpRequest, menuitem=0) -> HttpResponse:
    ''' показывает список заявок '''
    zavs =Zayavki.objects.filter(is_published=True).order_by('-time_create')
    filter_data={'filter_categ':'', 'filter_rentsale':'','price_from':'','price_to':'',}

    if  'filter_applied' in request.GET:
        import utils.apply_filter
        print(len(zavs))
        zavs = utils.apply_filter.go (request.GET, filter_data, zavs)
        print(len(zavs))
    context = {'items': zavs, 'user':request.user, 'menuitem':menuitem, 'sotr': True, "show_filter":1, "show_realty":0  }
    context.update(filter_data)
    return render(request=request, template_name='sotrud/requests.html', context=context)



#------------- страница одной заявки  -----------------------------------------------------------------

def itemreq (request: HttpRequest, id: int, menuitem=0) -> HttpResponse:
    ''' показывает страницу заявки со списком подходящих объктов'''
    #print("request.user.is_authenticated", request.user.is_authenticated)
    if request.user.is_authenticated:

        zav = Zayavki.objects.get(pk=id)
        okrug_str_titles = utils.get_okrug_titles.go(zav)
        rentsale=zav.rentsale
        if rentsale == "rent": pricetype = "руб./месяц";
        if rentsale == "sale": pricetype = "руб.";
        zavscan =zav.scan
        zavscan=zavscan.replace(' ', '')
        zavscan_list= zavscan.split(",")
        if len(zavscan)>0: result="Подходящие объекты по этой заявке"
        else: result="Для данной заявки нет подходящих объектов"

        realty_list=[]
        for zvi in zavscan_list:
            zvi_= zvi.split("-")

            if len(zvi)>1:
                realty_categ= str(zvi_[0])
                realty_id = str(zvi_[1])
                #получает объект по его id и категории
                item = Realtyitem_by_id_categ(realty_id,realty_categ)
                realty_list.append(item)
        if 'comment' in request.GET:
           zav.comment =  request.GET.get('comment')
           zav.save(update_fields=["comment"])

        context={"result": result, 'pricetype': pricetype,   'rentsale':rentsale,   'item': zav,  'menuitem':menuitem, "realties" : realty_list, 'okrug_str_titles': okrug_str_titles, 'sotr': True }
        return render(request=request, template_name='sotrud/podbor.html', context=context)
    else:
        return HttpResponse("нет доступа")


#-------------- ФОРМАТИРОВАНИЕ ФОТО -------------------------------------------------------------------

def formatfotos (request: HttpRequest,  menuitem=0) -> HttpResponse:

    if not request.user.is_authenticated:
        raise Exception ('Нет доступа к этой странице')

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


#-----  scan  ----------------------------------------------------------------------------

def scan (request: HttpRequest, menuitem=0) -> HttpResponse:
    ''' показывает станицу сканирования '''
    if request.user.is_authenticated:
        scanned=0
        counter_avito=''
        scan = Scanset.objects.get(pk=2)
        price_offset = scan.price_offset
        square_offset = scan.square_offset
        check_results=''

        if  'scan' in request.GET:


            # если нажата кнопка Сканировать
            fits_number=select(price_offset, square_offset)
            realty_bd_len, zavs_bd_len, all_realty = lenths()
            scan.zav_number = zavs_bd_len
            scan.realty_number = realty_bd_len
            scan.time_update=datetime.now()
            scan.save(update_fields=["zav_number", "realty_number","time_update"])

            scan = Scanset.objects.get(pk=2)
            check_zavs, check_realty, check, zav_number, realty_number = color_(scan, zavs_bd_len, realty_bd_len )
            scanned =1

            check_results=utils.check.go(all_realty)

            # avito
            import utils_export.avito_process
            counter_avito = utils_export.avito_process.go(all_realty)

        else:
            # если выбрана страница скан
            realty_bd_len, zavs_bd_len, all_realty = lenths()
            scan = Scanset.objects.get(pk=2)
            check_zavs, check_realty, check, zav_number, realty_number = color_(scan, zavs_bd_len, realty_bd_len )
            fits_number=""
        time_update = scan.time_update

        context = { 'fits_number': fits_number , 'check_results':check_results,  'scanned':scanned,'check_zavs':check_zavs,  'check_realty':check_realty,  'check':check, 'sotr': True, 'menuitem': menuitem, 'realty_number':realty_number, 'zav_number':zav_number, 'time_update':time_update, 'price_offset':price_offset, 'square_offset':square_offset, "realty_bd": realty_bd_len,"zavs_bd": zavs_bd_len, 'counter_avito':counter_avito }
        return render(request=request, template_name='sotrud/scan.html', context=context)

    else:
        return HttpResponse("нет доступа")

#----------показывает все объекты---------------------------------------------------

def allrealty  (request: HttpRequest,  menuitem=0) -> HttpResponse:
    ''' показывает список всех добавленных объктов'''

    if request.user.is_authenticated:
        realty_bd_len, zavs_bd_len, all_realty = lenths()
        all_realty.sort(reverse = True)
        context = {'realties': all_realty, "menuitem": menuitem}
        return render(request=request, template_name='sotrud/all_realty.html', context=context)
    else:
        return HttpResponse("нет доступа")

# ----------показывает заявки по данному объекту---------------------------------------------------

def showzavs (request: HttpRequest, menuitem=0, realty_id=0, realty_categ=0 ) -> HttpResponse:

    if request.user.is_authenticated:
        zavs=[]
        print("realty_id",realty_id)
        print("realty_categ",realty_categ )

        # получает объект по его id и категории
        item = Realtyitem_by_id_categ(realty_id, realty_categ)
        realtycan = item.scan
        realtycan_list = realtycan.split(",")
        print(realtycan_list)
        # realtycan_list - список заявок ро этому обекту

        for zav_id in realtycan_list:
            if len(zav_id) > 1:
                zav_id = zav_id.replace(' ', '')
                zav_id=int(zav_id)
                print("zav_id=", zav_id, type(zav_id))
                # получает заявку по id
                zav=Zayavki.objects.get(pk=zav_id)  # берет только одну запись
                zavs.append(zav)

        context = {'items': zavs, 'user': request.user, 'menuitem': menuitem, 'sotr': True, "realtyitem":item, "show_filter":0,  "show_realty":1 }

        return render(request=request, template_name='sotrud/requests.html', context=context)
    else:
        return HttpResponse("нет доступа")

# ----------показывает форму логин ---------------------------------------------------

class LoginUser (LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Логин пользователя'
        return context

# ----------  ---------------------------------------------------








