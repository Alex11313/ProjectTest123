import uuid
from django.db import models
from django.utils import timezone


def get_uid(model_name):
    def wrap():
        return str(uuid.uuid4) + model_name
    return wrap


class Department(models.Model):
    """
    Модель департамента
    """

    uid = models.CharField(default=get_uid('Department'), editable=False)
    name = models.CharField('Name', max_length=100, blank=True, null=True)
    #director = models.ForeignKey('employees.Employee', related_name='director',
    #                             on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Модель физического лица
    """

    uid = models.CharField(default=get_uid('Employee'), editable=False)
    name = models.CharField('Name', max_length=50)
    surname = models.CharField('Surname', max_length=50)
    patronymic = models.CharField('Patronymic', max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField('Creation_date', default=timezone.now)
    change_date = models.DateTimeField('Change_date', default=0.0)
    status = models.CharField('Status', default=0.0)
    type = models.CharField('Type', max_length=50)
    gender = models.CharField('Gender', max_length=50)
    timezone = models.CharField('Timezone', max_length=50)
    email = models.CharField('Email', max_length=50)
    phone = models.IntegerField('Phone', blank=True, null=True)
    addphone = models.IntegerField('Addphone', blank=True, null=True)
    socials = models.CharField('Socials', max_length=200)
    #department = models.ForeignKey('employees.Department', on_delete=models.SET_NULL, blank=True, null=True)
    #photo = models.FileField('Photo', upload_to='Employee/photo', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)


class Entity(models.Model):
    """
    Модель юридического лица
    """

    uid = models.CharField(default=get_uid('Entity'), editable=False)
    full_name = models.CharField('Full_name', max_length=100, blank=True, null=True)
    abb_name = models.CharField('Abb_name', max_length=50, blank=True, null=True)
    creation_date = models.DateTimeField('Creation_date', default=timezone.now)
    change_date = models.DateTimeField('Change_date', default=0.0)
    inn = models.IntegerField('Inn', blank=True, null=True)
    kpp = models.IntegerField('Kpp', blank=True, null=True)
    #director = models.ForeignKey('employees.Employee', related_name='director',
    #                             on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name