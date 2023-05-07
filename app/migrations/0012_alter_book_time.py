# Generated by Django 4.1.5 on 2023-05-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.IntegerField(choices=[(1, '11:00AM - 12:00AM'), (2, '12:00AM - 1:00PM'), (3, '1:00PM - 2:00PM'), (4, '2:00PM - 3:00PM'), (5, '3:00PM - 4:00PM'), (6, '4:00PM - 5:00PM'), (7, '5:00PM - 6:00PM'), (8, '6:00PM - 7:00PM'), (9, '7:00PM - 8:00PM'), (10, '8:00PM - 9:00PM'), (11, '9:00PM - 10:00PM')]),
        ),
    ]
