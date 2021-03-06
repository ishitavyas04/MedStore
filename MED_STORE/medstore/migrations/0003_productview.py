# Generated by Django 3.1.1 on 2020-11-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medstore', '0002_auto_20201120_1943'),
    ]

    operations = [
        migrations.CreateModel(
            name='Productview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medname', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='pics')),
                ('mrp', models.IntegerField(default=0)),
                ('discount', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=50)),
                ('shopname', models.CharField(max_length=50)),
                ('about', models.TextField(default='', max_length=200)),
            ],
        ),
    ]
