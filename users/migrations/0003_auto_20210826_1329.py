# Generated by Django 2.2.6 on 2021-08-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210802_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_superadmin',
            new_name='is_superuser',
        ),
    ]
