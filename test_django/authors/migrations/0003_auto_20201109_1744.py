# Generated by Django 3.1.2 on 2020-11-09 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_auto_20201109_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
