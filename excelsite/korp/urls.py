from django.urls import path
from .views import *
from django.views.static import serve

urlpatterns = [

    path('', page, name='home_ref', kwargs={"pagetitle": "О компании", "menuitem": 1001, }),
    path('userpage/', page, name='userpage_ref',kwargs={"pagetitle": "Страница пользователя", "menuitem": 1002, } ),

    path('home/', page, name='home_ref', kwargs={"pagetitle": "О компании", "menuitem": 1001, }),

    path('formsent/', formsent,  name="formsent_ref" ),
    path('category/<int:menu_id>/', items, name="ref"),

    path('item/ofis/<int:pk>/',   Item, name="itemref_ofis", kwargs={ "categ": "ofis", } ),
    path('item/torg/<int:pk>/',   Item, name="itemref_torg", kwargs={ "categ": "torg", }  ),
    path('item/tc/<int:pk>/',     Item, name="itemref_tc", kwargs={ "categ": "tc", }  ),
    path('item/proizv/<int:pk>/', Item, name="itemref_proizv", kwargs={ "categ": "proizv", }  ),
    path('item/sklad/<int:pk>/',  Item, name="itemref_sklad", kwargs={ "categ": "sklad", }  ),
    path('item/psn/<int:pk>/',    Item, name="itemref_psn", kwargs={ "categ": "psn", }  ),
    path('item/land/<int:pk>/',   Item, name="itemref_land", kwargs={ "categ": "land", }  ),
    path('item/flat/<int:pk>/',   Item, name="itemref_flat", kwargs={ "categ": "flat", }  ),

    path('search/', page, name='search_ref', kwargs={"pagetitle": "СТРАНИЦА В СТАДИИ РАЗРАБОТКИ", "menuitem": "search", }),


 ]



handler404 = pageNotFound
