# Generated by Django 5.0.3 on 2024-03-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
