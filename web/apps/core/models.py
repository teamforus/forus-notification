from django.db import models


# Create your models here.


class AppManager(models.Manager):
    def get_queryset(self):
        return super(AppManager, self).get_queryset()


class App(models.Model):
    name = models.CharField('name', max_length=1000)
    public_key = models.CharField('public_key', max_length=100)
    secrete_key = models.CharField('secrete_key', max_length=100)

    objects = AppManager()
