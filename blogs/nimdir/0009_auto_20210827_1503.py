# Generated by Django 2.2.6 on 2021-08-27 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20210827_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.CharField(default='', max_length=128),
        ),
    ]