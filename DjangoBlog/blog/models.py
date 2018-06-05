from django.db import models
import hashlib
from passlib.hash import sha256_crypt
# Create your models here.
class Blogpost(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_posted = models.DateField(db_index=True, auto_now_add=True)
    content = models.CharField(max_length=200)


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password_hash= models.CharField(max_length=200)
    last_login=models.DateField(auto_now=True)

    def encrypt_password(password):
        return  sha256_crypt.encrypt(password)

    def check_password(self, password):
        print("self "+self.password_hash)
        return sha256_crypt.verify(password, self.password_hash)
#$pbkdf2-sha256$29000$nBNiDKH0XquVUkopJaRUCg$htahMQPW23OsIcf.snm1XqOyEGDxMg..8Fk6c5kn.zk
