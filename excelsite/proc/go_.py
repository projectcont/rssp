from korp.models import Menu, Pages

def get_menu ():
    menu=Menu.objects.all().order_by('id')
    return menu

def get_pages (id):
    page=Pages.objects.get(pk=id)
    return page


