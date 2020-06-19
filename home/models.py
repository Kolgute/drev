from django.db import models
from django.utils.translation import gettext_lazy as _

class Home_block(models.Model):
    title = models.CharField(max_length=60,verbose_name=_('Заголовок'))
    body = models.TextField(blank=True, db_index=True,verbose_name=_('Описание'))
    first_button = models.CharField(max_length=15,verbose_name=_('Название первой кнопки'))
    second_button = models.CharField(max_length=15,verbose_name=_('Название второй кнопки'))
    image = models.ImageField(null=False,upload_to ='images/',verbose_name=_('Фоновая картинка'))

    def __str__(self):
        return '{}'.format(self.title)
    
    class Meta:
        verbose_name = _('Домашний блок')
        verbose_name_plural= _('1.Информация с первого блока(домашнего)')

class Welcome_block(models.Model):

    title = models.CharField(max_length=50,verbose_name=_('Заголовок'))
    about_title = models.CharField(max_length=50,verbose_name=_('Надпись под заголовком'))
    body = models.TextField(blank=True, db_index=True,verbose_name=_('Описание'))
    first_button = models.CharField(max_length=15,verbose_name=_('Название первой кнопки'))
    image = models.ImageField(null=False,upload_to ='images/',verbose_name=_('Картинка'))

    def __str__(self):
        return '{}'.format(self.title)
    class Meta:
        verbose_name = _('Приветствующий блок')
        verbose_name_plural= _('2.Информация с второго блока(Добро пожаловать)')


class Why_us(models.Model):
    title = models.CharField(max_length=50,verbose_name=_('Заголовок'))
    body = models.CharField(max_length=100,verbose_name=_('Описание'))
    icon = models.CharField(max_length=20,verbose_name=_('Иконка (fa fa icon))'))

    def __str__(self):
        return '{}'.format(self.title)
    class Meta:
        verbose_name = _('Почему мы')
        verbose_name_plural= _('3.Информация с третьего блока(Почему мы)')

class Service_block(models.Model):
    title = models.CharField(max_length=50,verbose_name=_('Заголовок'))
    body = models.TextField(blank=True, db_index=True,verbose_name=_('Описание'))
    first_button = models.CharField(max_length=15,verbose_name=_('Название кнопки'))
    image = models.ImageField(null=False,upload_to ='images/',verbose_name=_('Картинка'))

    def __str__(self):
        return '{}'.format(self.title)
    class Meta:
        verbose_name = _('Наш сервис')
        verbose_name_plural= _('4.Информация с четвёртого блока(Наше сервис)')

class Portfolio_block(models.Model):
    title = models.CharField(max_length=100,verbose_name=_('Описание'))
    image = models.ImageField(null=False,upload_to ='images/',verbose_name=_('Картинка'))

    def __str__(self):
        return '{}'.format(self.title)
    class Meta:
        verbose_name = _('Портфолио')
        verbose_name_plural= _('5.Информация с пятого блока(Портфолио)')

class Social_networks(models.Model):
    url = models.CharField(max_length=50,verbose_name=_('Ссылка'))
    icon = models.CharField(max_length=20,verbose_name=_('Иконка (fa fa icon)'))

    def __str__(self):
        return '{}'.format(self.icon)
    class Meta:
        verbose_name = _('Социальные сети')
        verbose_name_plural= _('6.Информация с шестого блока(Социальные сети)')

class Address_list(models.Model):
    address = models.CharField(max_length=50,verbose_name=_('Адресс'))

    def __str__(self):
        return '{}'.format(self.address)
    class Meta:
        verbose_name = _('Список адресов')
        verbose_name_plural= _('Информация со списком адресов')

class Phone_list(models.Model):
    phone = models.CharField(max_length=50,verbose_name=_('Телефон'))

    def __str__(self):
        return '{}'.format(self.phone)
    class Meta:
        verbose_name = _('Список номеров')
        verbose_name_plural= _('Информация со списком номеров')

class Email_list(models.Model):
    email = models.CharField(max_length=50,verbose_name=_('Емаил'))

    def __str__(self):
        return '{}'.format(self.email)
    class Meta:
        verbose_name = _('Список почт')
        verbose_name_plural= _('Информация со списком электронных почт')

class Contact_block(models.Model):
    addresses = models.ManyToManyField ('Address_list',blank=True,related_name='Address_list',verbose_name=_('Адреса'))
    phones = models.ManyToManyField ('Phone_list',blank=True,related_name='Phone_list',verbose_name=_('Телефоны'))
    emails = models.ManyToManyField ('Email_list',blank=True,related_name='Email_list',verbose_name=_('Емайлы'))

    def __str__(self):
        return 'Заполненный контакт'
    class Meta:
        verbose_name = _('Контакты')
        verbose_name_plural= _('7.Информация с последнего блока(Контакты)')

    