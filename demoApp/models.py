from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    surname = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    birthday = models.DateField(null=True)
    id_card = models.CharField(max_length=15,null=True)
    activ = models.BooleanField(default=False)
    descriptions = models.CharField(max_length=500,null=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    customs = models.CharField(max_length=100, null=True, blank=True)
    digit = models.CharField(max_length=20)
    id_card = models.CharField(max_length=20)
    activ = models.BooleanField(default=False)
    driver = models.ManyToManyField(User)
    descriptions = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Contract(models.Model):
    driver_id = models.ForeignKey(User, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.created
