from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date_service = models.DateTimeField('date service')

    def __str__(self):
        return self.first_name

class Car(models.Model):
    car_make = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    person = models.ForeignKey(Person, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return '%s: %s' % (self.car_make, self.car_model)

