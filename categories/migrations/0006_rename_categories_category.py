# Generated by Django 4.1.3 on 2022-11-21 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_category_and_more'),
        ('categories', '0005_alter_categories_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
