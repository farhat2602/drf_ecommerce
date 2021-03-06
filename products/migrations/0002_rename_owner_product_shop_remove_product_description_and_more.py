# Generated by Django 4.0.5 on 2022-06-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='owner',
            new_name='shop',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='extra_phone_num',
        ),
        migrations.RemoveField(
            model_name='product',
            name='phone_num',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
