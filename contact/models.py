from django.db import models
from django.utils import timezone

#id(primary key - automatico - feito pelo django)
#first_name, last_name, phone
#email, created, description

#Para fazer dps

#category(foreing key), show, owner(foreing key)
#picture
# Create your models here.

#Contact vai cirar, vuscar e deletar 
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=150) #poderia colocar blank = True pra ficar vazio
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank = True)
    show = models.BooleanField(default=True)
    #def pra mostrar no nome na lista de contatos
    def __str__(self):
        return f'{self.first_name} {self.last_name}'