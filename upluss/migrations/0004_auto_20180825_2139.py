# Generated by Django 2.1 on 2018-08-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upluss', '0003_auto_20180825_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livre',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
