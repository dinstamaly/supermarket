# Generated by Django 2.1.5 on 2019-03-18 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_billingprofile_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingprofile',
            name='order',
        ),
    ]
