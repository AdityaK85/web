# Generated by Django 4.1 on 2023-02-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0010_alter_dropdown_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='dropdown',
            name='payment',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]