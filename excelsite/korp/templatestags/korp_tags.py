from django import template
from korp.models import *

register=template.Library()

@register.simple_tag()
def get_menus():
    return Menu.objects.all()
