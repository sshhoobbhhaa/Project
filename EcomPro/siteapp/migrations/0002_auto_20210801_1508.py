# Generated by Django 3.2.4 on 2021-08-01 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='discription',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
