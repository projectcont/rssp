from django.urls import path
from .views import *
from django.views.static import serve

urlpatterns = [

    #path('clients/<int:menu_id>/', show_clients, name="clients_ref"),
    #path('requests/<int:pk>/', requests, name="requests_ref"),


    path('req/', requests, name="request_ref", kwargs={"menuitem": 1002, }),
    path('req/<int:id>', itemreq, kwargs={"menuitem": 1002, } ),
    path('allrealty/', allrealty, name="allrealty_ref", kwargs={"menuitem": 1007, }),

    path('formatfotos/', formatfotos, name="formatfotos_ref", kwargs={"menuitem": 1003,  }),


    path('scan/', scan, name="scan_ref", kwargs={"menuitem": 1006, }),
    path('showzavs/<int:realty_id>/<str:realty_categ>', showzavs, name="showzavs_ref", kwargs={"menuitem": 1008, }),

]

