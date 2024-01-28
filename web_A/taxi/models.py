from django.db import models
from phonenumber_field import modelfields
from django.contrib.auth import get_user_model
# Create your models here.
user = get_user_model()
class getposition_taxi_human(models.Model):
    taxiyour         = models.ForeignKey('Taxi_human',on_delete=models.CASCADE)
    position         = models.CharField(max_length= 100)
class Taxi_human(models.Model):
    taxiyour         = models.ForeignKey(user,on_delete=models.CASCADE)
    number_phone     = modelfields.PhoneNumberField(region="DZ")
