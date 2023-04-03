# Generated by Django 3.2.9 on 2023-03-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0003_questionmodel_max_puntaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choosequestionmodel',
            name='text',
            field=models.TextField(verbose_name='Answer text'),
        ),
        migrations.AlterField(
            model_name='questionmodel',
            name='max_puntaje',
            field=models.IntegerField(default=3, verbose_name='Maximo Puntaje'),
        ),
    ]
