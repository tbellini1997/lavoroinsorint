from django.conf.urls import url, include
from rest_framework import routers
from movierater.api import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('movierater.api.urls')),
]