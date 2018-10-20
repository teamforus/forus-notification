import uuid

from django.db import models

# Create your models here.
from fcm_django.models import FCMDevice


class UserConnectionFieldManager(models.Manager):
    def get_queryset(self):
        return super(UserConnectionFieldManager, self).get_queryset()

    def find_email_by_user(self, user):
        return super(UserConnectionFieldManager, self).filter(user=user)

    def find_emails_connection_by_user(self, user):
        return self.find_email_by_user(user).filter(type=UserConnectionField.EMAIL_TYPE).all()

    def get_or_create(self, reffer_id, type, value):
        user, created = User.objects.get_or_create(reffer_id=reffer_id)
        value = value.strip()
        if type == UserConnectionField.EMAIL_TYPE:
            connection = super(UserConnectionFieldManager, self).get_or_create(type=type, user=user)
            connection.value = value
            connection.save()
        else:
            connection = super(UserConnectionFieldManager, self).get_or_create(type=type, user=user, value=value)

        return connection


class UserConnectionFCMDeviceManager(models.Manager):
    def get_queryset(self):
        return super(UserConnectionFCMDeviceManager, self).get_queryset()

    def get_or_create_by_connection(self, user_connection):
        fcm_device, created = FCMDevice.objects.get_or_create(
            registration_id=user_connection.value,
            defaults={'device_id': uuid.uuid4(), 'type': 'ios', 'name': user_connection.user.reffer_id, 'active': True}
        )
        return self.get_queryset().get_or_create(user_connection=user_connection, device=fcm_device)


class User(models.Model):
    reffer_id = models.CharField('Id', max_length=1000)

    def __str__(self):
        return self.reffer_id


class UserConnectionField(models.Model):
    EMAIL_TYPE = 1
    FIREBASE_TYPE = 2

    TYPE_CHOICES = (
        (EMAIL_TYPE, 'Email'),
        (FIREBASE_TYPE, 'Firebase'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    value = models.CharField('value', max_length=1000)

    type = models.IntegerField(choices=TYPE_CHOICES, default=EMAIL_TYPE)

    objects = UserConnectionFieldManager()


class UserConnectionFCMDevice(models.Model):
    user_connection = models.ForeignKey(UserConnectionField, on_delete=models.CASCADE, blank=False, null=True)
    device = models.ForeignKey(FCMDevice, on_delete=models.CASCADE, blank=False, null=True)

    objects = UserConnectionFCMDeviceManager()
