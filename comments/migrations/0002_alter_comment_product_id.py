# Generated by Django 4.1.3 on 2022-12-11 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product'),
        ),
    ]
