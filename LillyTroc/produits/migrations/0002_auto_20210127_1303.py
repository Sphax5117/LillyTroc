# Generated by Django 3.1.5 on 2021-01-27 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='templates/produits/images'),
        ),
    ]
