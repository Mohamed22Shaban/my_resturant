# Generated by Django 2.1.2 on 2018-12-29 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0043_auto_20181228_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='helos',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
