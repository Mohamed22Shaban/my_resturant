# Generated by Django 2.1.2 on 2018-12-07 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0018_menuitem_selcted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='selcted',
        ),
    ]
