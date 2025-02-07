from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#id(primary key - automatico - feito pelo django)
#first_name, last_name, phone
#email, created, description
#category(foreing key), show, owner(foreing key)
#picture

#Para fazer dps
#owner
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    
    class Meta:#Classe para arrumar o plural
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
    
#Contact vai cirar, vuscar e deletar 
class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=150) #poderia colocar blank = True pra ficar vazio
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank = True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    #category = models.CharField(max_length=20) jeito de não ser feito porque seria feito uma a uma
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, blank=True, null=True) #CASCADE no lugar do set_null seria para quando apagar uma categoria ela apagar tudo dentro dela
    owner = models.ForeignKey(User, on_delete= models.SET_NULL, blank=True, null=True)
    
    #def pra mostrar no nome na lista de contatos
    def __str__(self):
        return f'{self.first_name} {self.last_name}'