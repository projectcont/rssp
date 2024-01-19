from korp.models import Realty
''' '''

class Avito():
    def __init__(self):
        self.id = None
        self.description = None

    def set_description(self, value):
        if '222' in value :
            print('good')
            self.description = value
        else:
            print('no good')



def Avito_xml_item (item):
    avito.set_description(item.content)
    result=0
    return  result

def Avito_items (items):
    for item in items:
        result=''
        if result==1:
            Avito_xml_item(item)
        else:pass



    return None
