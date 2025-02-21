from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    #pego a url do projeto principal que fica fixada aqui
    path('<int:contact_id>/', views.contact, name='contact' ),
    path("search/", views.search, name="search"),
    path('', views.index, name='index' ),
]
