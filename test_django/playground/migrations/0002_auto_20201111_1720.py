# Generated by Django 3.1.2 on 2020-11-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='pass_id',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]