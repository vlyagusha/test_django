# Generated by Django 3.1.2 on 2020-11-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_auto_20201112_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]