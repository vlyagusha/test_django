# Generated by Django 3.1.2 on 2020-11-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AuthorsModel',
            new_name='Author',
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='email_address',
            new_name='email',
        ),
    ]
