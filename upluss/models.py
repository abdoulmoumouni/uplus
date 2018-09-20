from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Livre(models.Model):
    date_ajout = models.DateTimeField(auto_now_add=True)
    titre = models.CharField(max_length = 150)
    auteur = models.CharField(max_length = 150)
    editeur = models.CharField(max_length = 150)
    etat = models.CharField(max_length = 8)
    description = RichTextField(blank=True, null=True)
    prix = models.IntegerField()
    vote = models.IntegerField()
    image = models.ImageField(upload_to ="images/")
    categorie = models.CharField(max_length = 100)
    pages = models.IntegerField()
    date_parution=models.DateTimeField(auto_now_add=False)
    resume = models.TextField()
    sommaire = RichTextField(blank=True, null=True)
    caracteristique = RichTextField(blank=True, null=True)
    point_vente = models.IntegerField()
    hunter = models.ForeignKey(User,on_delete = models.CASCADE)


    def summary(self):
        return self.description[:140]


class Infos(models.Model):
    date_ajout = models.DateTimeField(auto_now_add=True)
    universite = models.CharField(max_length = 150)
    faculte = models.CharField(max_length = 150)
    slug = models.SlugField(blank=True)
    categorie = models.CharField(max_length = 150)
    titre = models.CharField(max_length = 150)
    image = models.ImageField(upload_to ="images/")
    description = models.TextField()
    date_parution = models.DateTimeField(auto_now_add=False)
    signature1 = models.CharField(max_length = 150)
    hunter = models.ForeignKey(User,on_delete = models.CASCADE)

    def descarac(self):
        return self.description[:168]

    def get_absolute_url(self):
        return reverse('detailinfo', args=[str(self.id)])
