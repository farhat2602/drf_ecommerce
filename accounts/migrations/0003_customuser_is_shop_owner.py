# Generated by Django 4.0.5 on 2022-06-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_ip_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_shop_owner',
            field=models.BooleanField(default=False),
        ),
    ]
