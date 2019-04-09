from django.conf import settings
from django.db import models
from django.utils import timezone


class Users(models.Model):
    _id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __getid__(self):
        return self.id
'''
    По аналогии надо саздать классы под каждую таблицу:
        3 вида теплиц
        юзеры
        что там еще
'''
