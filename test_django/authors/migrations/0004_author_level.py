# Generated by Django 3.1.2 on 2020-11-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20201109_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='level',
            field=models.CharField(choices=[('J', 'Junior'), ('M', 'Middle'), ('S', 'Senior')], default='J', max_length=1),
            preserve_default=False,
        ),
    ]
