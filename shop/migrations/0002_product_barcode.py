# Generated by Django 3.0.6 on 2020-06-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.TextField(default='<built-in function id>', max_length=48),
        ),
    ]
