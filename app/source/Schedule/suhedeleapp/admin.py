from django.contrib import admin
from .models import Todolist, Userlist

# Register your models here.

admin.site.register(Todolist)
admin.site.register(Userlist)