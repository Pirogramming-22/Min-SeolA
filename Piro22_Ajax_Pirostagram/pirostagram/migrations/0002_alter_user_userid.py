# Generated by Django 5.1.5 on 2025-01-19 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirostagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userid',
            field=models.CharField(max_length=20, unique=True, verbose_name='아이디'),
        ),
    ]
