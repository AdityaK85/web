# Generated by Django 4.1 on 2022-10-02 12:31

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0004_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='new_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique=True),
        ),
    ]
