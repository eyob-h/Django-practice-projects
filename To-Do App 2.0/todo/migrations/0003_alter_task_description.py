# Generated by Django 5.0.2 on 2024-02-15 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_task_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.CharField(default='', max_length=400),
        ),
    ]
