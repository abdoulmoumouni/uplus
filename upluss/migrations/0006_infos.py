# Generated by Django 2.1 on 2018-08-29 17:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upluss', '0005_auto_20180825_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('universite', models.CharField(max_length=150)),
                ('faculte', models.CharField(max_length=150)),
                ('categorie', models.CharField(max_length=150)),
                ('titre', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField()),
                ('date_parution', models.DateTimeField()),
                ('signature1', models.CharField(max_length=150)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
