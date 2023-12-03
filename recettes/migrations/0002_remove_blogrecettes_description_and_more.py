# Generated by Django 4.2.5 on 2023-10-27 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recettes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogrecettes',
            name='description',
        ),
        migrations.AddField(
            model_name='blogrecettes',
            name='ingredient',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='blogrecettes',
            name='recipe',
            field=models.TextField(max_length=400, null=True),
        ),
    ]
