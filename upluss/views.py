from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import auth
from .models import Livre
from .models import Infos
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    pub = Infos.objects.order_by('-date_ajout')
    paginator = Paginator(pub, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    pub = paginator.get_page(page)
    context={'pub':pub}
    return render(request,'uplus/index.html',context)

# Login page
def login(request):
    if request.method == "POST":
        user=auth.authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'Bienvenue :')
            return redirect ('index')
        else:
            return render(request,'uplus/login.html',{'erreur':'Nom d\'utilisateur ou mot de pass errone' })
    else:
        return render(request,'uplus/login.html')


# logout page
def logout_user(request):
    logout(request)
    return redirect('login')


# register page
def register(request):
    if request.method =="POST":
        if request.POST['password'] == request.POST['repassword']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'uplus/register.html',{'erreur':'Utilisateur deja occupe' })
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],first_name=request.POST['prenom'],last_name=request.POST['nom'],password=request.POST['password'],email=request.POST['email'])
                auth.login(request,user)
                return redirect('login')
        else:
            return render(request,'uplus/register.html',{'erreur':'les mots de pass ne correspondent pas' })
    else:
        return render(request,'uplus/register.html')

#pages des livres
def librairie(request):
    book = Livre.objects.order_by('-date_ajout')
    paginator = Paginator(book, 3) # Show 25 contacts per page
    page = request.GET.get('page')
    book = paginator.get_page(page)
    context = {'book':book}
    return render(request,'uplus/librairie.html',context)


#pages lock screen
def lockscreen(request):
    return render(request,'uplus/lockscreen.html')

#pages profile
def profil(request):
    return render(request,'uplus/profil.html')

#pages edition du profile
def edit_profil(request):
    return render(request,'uplus/edit_profil.html')

#pages detail livre
def detail(request, livre_id):
    livre = get_object_or_404(Livre, pk=livre_id)
    return render(request,'uplus/detail.html',{'livre': livre})

#pages detail infos
def detailinfo(request, infos_id):
    info = get_object_or_404(Infos, pk=infos_id)
    return render(request,'uplus/detailinfo.html',{'info': info})

#uam
def uam(request):
    info = Infos.objects.filter( universite ="UAM")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/uam.html',context)

#udd
def uddinfo(request):
    info = Infos.objects.filter( universite ="UDD")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/uddinfo.html',context)
#uz
def uz(request):
    info = Infos.objects.filter( universite ="UZ")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/uz.html',context)

#ut
def ut(request):
    info = Infos.objects.filter( universite ="UT")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/ut.html',context)

#ua
def ua(request):
    info = Infos.objects.filter( universite ="UA")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/ua.html',context)

#uti
def uti(request):
    info = Infos.objects.filter( universite ="UTI")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/uti.html',context)

#ud
def ud(request):
    info = Infos.objects.filter( universite ="UD")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/ud.html',context)

#ud
def udi(request):
    info = Infos.objects.filter( universite ="UDI")
    paginator = Paginator(info, 15) # Show 25 contacts per page
    page = request.GET.get('page')
    info = paginator.get_page(page)
    context = {'info':info}
    return render(request,'uplus/udi.html',context)
