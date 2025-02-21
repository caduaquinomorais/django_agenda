from django.http import Http404
from django.shortcuts import render, get_object_or_404
from contact.models import Contact
# Create your views here.


def index(request):
    contacts = Contact.objects.all().order_by('-id')#Visualizar o id pelo ultimo
    #no lugar do all, posso usar o filter(show=true) onde o show true é uma escolha na pagina do admin pra mostrar ou não o contato. Além disso, posso colocar outros filtros
    context = {
        'contacts': contacts,
        'site_title': 'Contatos - '
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )

def contact(request,contact_id):
    ##single_contact = Contact.objects.filter(pk= contact_id).first() / Depois do = eu posso passar assim embaixo também ou como já foi passado
    
    ##if single_contact is None:
        ##raise Http404()
    #Ao invés de fazer como a cima que seria na "unha", existe algo pronto do Django

    single_contact = get_object_or_404(Contact, pk= contact_id, show = True )
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'site_title': contact_name
    } 
    
    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request):
    search_value = request.GET
    

    contacts = Contact.objects.all().order_by('-id')#Visualizar o id pelo ultimo
    context = {
        'contacts': contacts,
        'site_title': 'Search - '
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )