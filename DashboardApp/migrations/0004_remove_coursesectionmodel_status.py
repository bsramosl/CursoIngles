# Generated by Django 3.2.9 on 2023-04-27 02:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0003_auto_20230421_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesectionmodel',
            name='status',
        ),
    ]
