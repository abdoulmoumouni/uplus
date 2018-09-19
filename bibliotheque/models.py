from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Bibliotheque(models.Model):
    date_ajout = models.DateTimeField(auto_now_add = True)
    titre = models.CharField(max_length = 150)
    auteur = models.CharField(max_length = 150,blank=True, null=True)
    type = models.CharField(max_length = 150,blank=True, null=True)
    structure = models.CharField(max_length = 150,blank=True, null=True)
    utilisateur = models.ForeignKey(User,on_delete = models.CASCADE,blank=True, null=True)
    logo = models.ImageField(upload_to ="images/",blank=True, null=True)
    image = models.ImageField(upload_to ="images/" ,blank=True, null=True )
    corps = RichTextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('detailbiblio', args=[str(self.id)])
