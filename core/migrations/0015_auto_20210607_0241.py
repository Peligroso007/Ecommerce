# Generated by Django 3.1.6 on 2021-06-07 02:41

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_order_billing_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='countries',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(default='china', max_length=2),
            preserve_default=False,
        ),
    ]