# Generated by Django 5.1.4 on 2025-01-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devtool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devtool',
            name='content',
            field=models.TextField(verbose_name='설명'),
        ),
    ]
