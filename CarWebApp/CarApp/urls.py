from django.conf.urls import include, url
from . import views

urlpatterns = [
    url('index/', views.index, name='index'),
    url('details/(?P<id>[0-9]+)$', views.details, name='details'),

    url('register/', views.register, name='register'),
    url('login/', views.login, name='login'),
    url('logout/', views.logout, name='logout'),

]
