# Generated by Django 3.2.6 on 2021-08-23 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='result',
            field=models.CharField(max_length=400, null=True, verbose_name='result'),
        ),
    ]
