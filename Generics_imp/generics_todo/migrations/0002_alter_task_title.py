# Generated by Django 4.2.10 on 2024-03-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generics_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
