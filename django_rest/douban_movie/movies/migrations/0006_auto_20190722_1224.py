# Generated by Django 2.2.3 on 2019-07-22 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20190722_1223'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='doubanmovie',
            table='douban_movie',
        ),
    ]
