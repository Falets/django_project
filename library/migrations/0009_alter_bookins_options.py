# Generated by Django 4.1 on 2022-11-15 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_delete_rent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookins',
            options={'ordering': ['status'], 'permissions': (('can_change', 'Set book as returned'),)},
        ),
    ]
