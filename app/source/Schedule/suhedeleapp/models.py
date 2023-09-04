from django.db import models
from django.utils import timezone

# Create your models here.

class Todolist(models.Model):
    day = models.DateField('日付け', default= timezone.now)
    content = models.CharField('予定', max_length=50)
    

    def __str__(self):
        return '<id:' + str(self.id) + ',' + self.content + '>'



# class Userlist(models.Model):
#     name = models.CharField('名前',  max_length=20)
#     password = models.CharField('パスワード', max_length=50)

#     def __str__(self):
#         return '<id:' + str(self.name) + ',' + self.password + '>'
    