# Generated by Django 3.2.9 on 2023-04-21 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DashboardApp', '0002_auto_20230405_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='level',
            field=models.CharField(choices=[('BASIC', 'BASIC'), ('INTERMEDIATE', 'INTERMEDIATE'), ('ADVANCE', 'ADVANCE')], default='basic', max_length=12),
        ),
        migrations.CreateModel(
            name='CourseSectionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('description', models.TextField(verbose_name='Description')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DashboardApp.coursemodel')),
            ],
            options={
                'verbose_name': 'CourseSection',
                'verbose_name_plural': 'CoursesSections',
                'ordering': ['id'],
            },
        ),
    ]