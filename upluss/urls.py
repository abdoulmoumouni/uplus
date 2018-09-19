from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login,name="login"),
    path('<int:livre_id>/', views.detail, name='detail'),
    path('infos/<int:infos_id>/', views.detailinfo, name='detailinfo'),
    path('index', views.index,name="index"),
    path('index/uam', views.uam,name="uam"),
    path('index/uddinfo', views.uddinfo,name="uddinfo"),
    path('index/uz', views.uz,name="uz"),
    path('index/ut', views.ut,name="ut"),
    path('index/ua', views.ua,name="ua"),
    path('index/uti', views.uti,name="uti"),
    path('index/ud', views.ud,name="ud"),
    path('index/udi', views.udi,name="udi"),
    path('logout', views.logout_user,name="logout"),
    path('register', views.register,name="register"),
    path('lockscreen', views.lockscreen,name="lockscreen"),
    path('profil', views.profil,name="profil"),
    path('edit_profil', views.edit_profil,name="edit_profil"),
    path('librairie', views.librairie,name="librairie"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
