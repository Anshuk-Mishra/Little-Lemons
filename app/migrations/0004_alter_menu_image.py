# Generated by Django 4.1.5 on 2023-05-01 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_menu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='uploads/'),
        ),
    ]
