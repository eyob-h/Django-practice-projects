# Generated by Django 5.0.3 on 2024-03-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
