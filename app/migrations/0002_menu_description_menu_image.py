# Generated by Django 4.1.5 on 2023-05-01 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default='hello.jpg', upload_to='', verbose_name='uploads/'),
            preserve_default=False,
        ),
    ]
