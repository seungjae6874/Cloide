# Generated by Django 3.1.1 on 2020-09-20 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='author',
            field=models.CharField(default='simple', max_length=100),
        ),
    ]
