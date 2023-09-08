
from django.urls import path
from .views import *


urlpatterns = [

    path('', company),
    path('home/', company, name='home_ref'),
    path('contacts/', contacts, name='contacts_ref'),
    path('form/', form, name='form_ref'),
    path('login/', login, name='login_ref'),

    path('events/', events, name='events_ref'),
    path('proj/<int:post_id>/', event, name="proj_ref"),
    path('postevent/', postevent, name='postevent_ref'),

    path('project/', project, name='projects_ref'),

    path('category/<int:categ_id>/', categs, name="category_ref"),
]

handler404=pageNotFound
