# Generated by Django 3.2.9 on 2023-03-21 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0002_preguntasrespondidas_quizuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionmodel',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6, verbose_name='Maximo Puntaje'),
        ),
    ]
