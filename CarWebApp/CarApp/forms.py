from django import forms
from .models import User, CarBook
from .views import *
import datetime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class RegisterForm(forms.ModelForm):

    class Meta:

        model = User

        fields = ('first_name','last_name','username', 'email','password')
        widgets = {
        'password': forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):

    class Meta:

        model = User

        fields=('username','password')
        widgets = {
        'password': forms.PasswordInput(),
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = CarBook

        fields=('frombooked','tobooked','note')
        #bookfrom = forms.DateField(label='Da:',widget=forms.SelectDateWidget(),  initial=datetime.date.today())
        #bookto = forms.DateField(label='a:',widget=forms.SelectDateWidget(),  initial=datetime.date.today())
        #note = forms.CharField(widget=forms.Textarea)
