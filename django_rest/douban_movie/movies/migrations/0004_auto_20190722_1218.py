# Generated by Django 2.2.3 on 2019-07-22 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20190722_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoubanMovie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('img_url', models.CharField(max_length=200)),
                ('rate', models.FloatField()),
                ('detail_url', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'douban_movie',
            },
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]