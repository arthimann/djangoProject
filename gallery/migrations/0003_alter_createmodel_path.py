# Generated by Django 4.1.3 on 2022-12-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_createmodel_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createmodel',
            name='path',
            field=models.FileField(upload_to='images/'),
        ),
    ]
