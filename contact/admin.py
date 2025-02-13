from django.contrib import admin
from contact import models
from contact.models import Contact
# Register your models here.
#configuração do model na admin do django
@admin.register(models.Contact)
class ContactAdmin (admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','show')
    ordering= ('-id',)#ordenando por id contrário para os mais novos ficarem no começo
    search_fields = ('id','first_name',)
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name','show'
    list_display_links = 'phone',
    
    
@admin.register(models.Category)
class CategorytAdmin (admin.ModelAdmin):
    list_display = ('name',)
    ordering= ('-id',)