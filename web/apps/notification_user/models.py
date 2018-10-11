from django.db import models


# Create your models here.



class User(models.Model):
    reffer_id = models.CharField('Id', max_length=1000)

    def __str__(self):
        return self.id
