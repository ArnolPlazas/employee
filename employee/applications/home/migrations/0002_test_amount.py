# Generated by Django 3.2 on 2023-02-19 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='amount',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
