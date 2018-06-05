from django.db import models
import hashlib
from django import forms
from passlib.hash import sha256_crypt
from django.core.validators import MinLengthValidator
from datetime import date

# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password= models.CharField(max_length=200, validators=[MinLengthValidator(4)])
    last_login=models.DateField(auto_now=True)

    def encrypt_password(pwd):
        return  sha256_crypt.encrypt(pwd)

    def check_password(self, pwd):
        print("self "+self.password)
        return sha256_crypt.verify(pwd, self.password)

    def __str__(self):
        return self.username


class Car(models.Model):
    name=models.CharField(max_length=200) #nome veicolo
    model=models.CharField(max_length=200) #modello
    licenseplate=models.CharField(max_length=200) #targa
    doors=models.CharField(max_length=200) #portiere
    seats=models.CharField(max_length=200) #posti a sedere
    booked=models.BooleanField(default=False)

    def __str__(self):
        return self.model

class CarBooked(models.Model):
    frombooked = models.DateField(default=date.today)
    tobooked = models.DateField(default=date.today)
    note = models.TextField(default="Aggiungi note..")

    username = models.ForeignKey(User,on_delete=models.CASCADE)
    model = models.ForeignKey(Car,on_delete=models.CASCADE)
