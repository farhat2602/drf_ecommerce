# Generated by Django 4.0.5 on 2022-06-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customuser_is_admin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
