from korp.models import Menu
item1=Menu (title='О компании',url='/home')
item2=Menu (title='Расписание курсов', url='/kurses')
item3=Menu (title='Форма заявки', url='/form')
item4=Menu (title='Личный кабинет', url='/login')
item5=Menu (title='Контакты', url='/form')
item1.save()
item2.save()
item3.save()
item4.save()
item5.save()

О компании
Расписание курсов
Форма заявки
Личный кабинет
Контакты