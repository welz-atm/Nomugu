# Generated by Django 3.0.4 on 2020-10-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
