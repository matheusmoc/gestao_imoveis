# Generated by Django 4.2 on 2023-05-17 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ProductImage',
        ),
    ]