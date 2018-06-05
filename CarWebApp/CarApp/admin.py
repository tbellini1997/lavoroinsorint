from django.contrib import admin
from .models import User, Car, CarBook
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class CarAdmin(admin.ModelAdmin):
    pass
admin.site.register(Car,CarAdmin)

class CarBookedAdmin(admin.ModelAdmin):
    pass
admin.site.register(CarBook,CarBookedAdmin)
