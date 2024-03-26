# Generated by Django 4.2.10 on 2024-03-19 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('generics_todo', '0004_task_apiuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='apiuser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]