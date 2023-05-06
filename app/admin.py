from django.contrib import admin
from app import models

class AdminMenu(admin.ModelAdmin):
    list_display = ['name','price']

class AdminBook(admin.ModelAdmin):
    list_display = ["Fname","date","time"]    
# Register your models here.
admin.site.register(models.Menu,AdminMenu)
admin.site.register(models.Book,AdminBook)