# Generated by Django 2.0 on 2020-02-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='0'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.TextField(default='title'),
        ),
    ]