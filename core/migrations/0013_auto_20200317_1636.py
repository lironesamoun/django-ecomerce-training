# Generated by Django 3.0.4 on 2020-03-17 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200317_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='items',
            new_name='item',
        ),
    ]
