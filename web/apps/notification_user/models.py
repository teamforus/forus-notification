from django.db import models


# Create your models here.

class UserConnectionFieldManager(models.Manager):
    def get_queryset(self):
        return super(UserConnectionFieldManager, self).get_queryset()

    def find_email_by_user(self, user):
        return super(UserConnectionFieldManager, self).filter(user=user)

    def find_emails_connection_by_user(self, user):
        return self.find_email_by_user(user).filter(type=UserConnectionField.EMAIL_TYPE).all()

    def get_or_create(self, reffer_id, type, value):
        user, created = User.objects.get_or_create(reffer_id=reffer_id)
        connection = super(UserConnectionFieldManager, self).get_or_create(type=type, user=user, value=value.strip())

        return connection


class User(models.Model):
    reffer_id = models.CharField('Id', max_length=1000)

    def __str__(self):
        return self.reffer_id


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

    objects = UserConnectionFieldManager()
