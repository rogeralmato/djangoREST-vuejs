from django.db import models
from django.contrib.auth.models import User  


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField('First Name', max_length=100)
    last_name = models.CharField('Last Name', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"