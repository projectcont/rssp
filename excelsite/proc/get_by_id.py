from korp.models import *

def get_realty_by_id(id):
    result = Realty.objects.get(pk=id)
    return result

def get_category_by_id(id):
    result = Category.objects.get(pk=id)
    return result

def get_page_by_id(id):
    result = Pages.objects.get(pk=id)
    return result