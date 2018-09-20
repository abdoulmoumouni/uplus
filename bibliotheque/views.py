from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Bibliotheque


# Create your views here.
def biblio(request):
    document = Bibliotheque.objects.all()
    paginator = Paginator(document, 4) # Show 25 contacts per page
    page = request.GET.get('page')
    document = paginator.get_page(page)
    context = {
        'document':document
    }
    return render (request,'bibliotheque/biblio.html',context)

#pages detail livre
def detailbiblio(request, bibliotheque_id):
    bibliotheque = get_object_or_404(Bibliotheque, pk = bibliotheque_id)
    return render(request,'bibliotheque/detailbiblio.html',{'bibliotheque': bibliotheque})

def searchbiblio(request):
    query = request.GET.get('query')
    if not query:
        biblio = Bibliotheque.objects.all()
    else:
        # titre contains the query is and query is not sensitive to case.
        biblio = Bibliotheque.objects.filter(titre__icontains=query)
    if not biblio.exists():
        biblio = Bibliotheque.objects.filter(auteur__name__icontains=query)
    titre = "Resultats pour la requete %s"%query
    context = {
        'biblio': biblio,
        'titre': titre
    }
    return render(request, 'bibliotheque/searchbiblio.html', context)
