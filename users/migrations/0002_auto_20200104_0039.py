# Generated by Django 3.0.1 on 2020-01-03 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': 'Users info'},
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='check_emali',
            new_name='check_email',
        ),
    ]
