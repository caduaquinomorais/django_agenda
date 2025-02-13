from django.shortcuts import render
from contact.models import Contact
# Create your views here.



def index(request):
    contacts = Contact.objects.all().order_by('-id')#Visualizar o id pelo ultimo
    #no lugar do all, posso usar o filter(show=true) onde o show true é uma escolha na pagina do admin pra mostrar ou não o contato. Além disso, posso colocar outros filtros
    context = {
        'contacts': contacts
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )