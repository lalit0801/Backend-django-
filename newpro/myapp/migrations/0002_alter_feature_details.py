# Generated by Django 4.2.10 on 2024-02-21 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='details',
            field=models.CharField(max_length=500),
        ),
    ]
