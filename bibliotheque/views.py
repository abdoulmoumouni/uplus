from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Bibliotheque


# Create your views here.
def biblio(request):
    document = Bibliotheque.objects.all()
    paginator = Paginator(document, 15) # Show 25 contacts per page
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
