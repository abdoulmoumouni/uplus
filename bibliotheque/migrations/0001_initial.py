# Generated by Django 2.1 on 2018-09-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bibliotheque',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('titre', models.CharField(max_length=150)),
                ('auteur', models.CharField(max_length=150)),
            ],
        ),
    ]
