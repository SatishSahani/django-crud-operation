from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')
    
# @admin.register(MobileLoginForm)    
# class Mobile(admin.ModelAdmin):
#         list_display2=('id','Phone Number','Password')