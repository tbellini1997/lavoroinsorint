from django import forms
from .models import Blogpost, User
from .views import *
class PostForm(forms.ModelForm):

    class Meta:
        model = Blogpost
        fields = ('title','subtitle','author','content',)

class SignForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password_hash')

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password_hash')
