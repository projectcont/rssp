from django import template
from korp.models import *

register=template.Library()

@register.simple_tag()
def get_menus(chosen=0):
    menus = Menu.objects.all()
    vt=[]
    for v in menus:
        vt.append(v.title)
    return vt
