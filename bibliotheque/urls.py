from django.conf.urls import url
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.biblio,name="biblio"),
    path('searchbiblio', views.searchbiblio,name="searchbiblio"),
    path('<int:bibliotheque_id>/', views.detailbiblio, name='detailbiblio'),

    # path('infos/<int:infos_id>/', views.detailinfo, name='detailinfo'),
    # path('index', views.index,name="index"),
    # path('logout', views.logout_user,name="logout"),
    # path('register', views.register,name="register"),
    # path('lockscreen', views.lockscreen,name="lockscreen"),
    # path('profil', views.profil,name="profil"),
    # path('edit_profil', views.edit_profil,name="edit_profil"),
    # path('librairie', views.librairie,name="librairie"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
