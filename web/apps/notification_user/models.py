from django.db import models


# Create your models here.





class User(models.Model):
    reffer_id = models.CharField('Id', max_length=1000)

    def __str__(self):
        return self.id


class UserConnectionField(models.Model):
    EMAIL_TYPE = 1
    GCS_TYPE = 2
    TYPE_CHOICES = (
        (EMAIL_TYPE, 'Email'),
        (GCS_TYPE, 'Google cloud message'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    value = models.CharField('value', max_length=1000)

    type = models.IntegerField(choices=TYPE_CHOICES, default=EMAIL_TYPE)
