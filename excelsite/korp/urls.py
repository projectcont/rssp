
from django.urls import path
from .views import *


urlpatterns = [

    path('', company),
    path('home/', company),
    path('projects/', projects),
    path('contacts/', contacts),
    path('form/', form),
    path('kurses/', kurses),
    path('login/', login),
]

handler404=pageNotFound
