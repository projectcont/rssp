"""
URL configuration for excelsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from excelsite import settings
from korp import views as  korpviews

from django.views.static import serve

urlpatterns = [
    #path('/', include('korp.urls')),
    path('', korpviews.page,  kwargs={"pagetitle": "О компании", "menuitem": 1001, }),
    path('userlux/', admin.site.urls),
    path('korp/', include('korp.urls')),
    path('crm/', include('crm.urls')),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns.extend(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.XML_URL, document_root=settings.XML_ROOT)


