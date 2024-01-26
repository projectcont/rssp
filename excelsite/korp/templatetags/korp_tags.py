from django import template
from korp.models import *
import decimal


register=template.Library()


@register.filter(name='space_format')
def del_comma(value):
    if isinstance(value, int) or isinstance(value, float) or isinstance(value, decimal.Decimal)  :
        x2 = str(int(value))
        xv = x2[-18:-15] + " " + x2[-15:-12] + " " + x2[-12:-9] + " " + x2[-9:-6] + " " + x2[-6:-3] + " " + x2[-3:]
        return xv
    else:
        value='не указано'
    return value


@register.simple_tag()
def get_map(map:str):
    #width = "560"
    #height = "400"
    #frameborder = "1"
    map=map.replace('width = "560"', 'width = "100%"')
    map = map.replace('height = "400"', 'height = "500"')
    map = map.replace('frameborder = "1"', 'frameborder = "0"')
    return map



