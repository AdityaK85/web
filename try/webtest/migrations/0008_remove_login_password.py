# Generated by Django 4.1 on 2022-10-20 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0007_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='password',
        ),
    ]
