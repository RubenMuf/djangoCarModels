from django.db import models

# Create your models here. Создаем объект на основе класса
class Car(models.Model):
    stamp = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=10)
    release_date = models.IntegerField()
    state_number = models.CharField(max_length=10)
