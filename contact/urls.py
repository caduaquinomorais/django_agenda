from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    #pego a url do projeto principal que fica fixada aqui
    path('', views.index, name='index' ),
]
