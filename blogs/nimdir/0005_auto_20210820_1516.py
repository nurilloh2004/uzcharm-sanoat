# Generated by Django 2.2.6 on 2021-08-20 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_foreignrepresentativeitems_foreignrepresentativeitemstranslation_foreignrepresentativelinks_foreignr'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreignrepresentativeitems',
            name='link',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='blogs.ForeignRepresentativeLinks', verbose_name='link'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foreignrepresentativeitems',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='icons/', verbose_name='icon'),
        ),
    ]
