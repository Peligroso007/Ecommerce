# Generated by Django 2.2.8 on 2020-10-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201005_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
