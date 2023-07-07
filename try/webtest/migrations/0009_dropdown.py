# Generated by Django 4.1 on 2023-02-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0008_remove_login_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='dropdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personality', models.CharField(choices=[('', 'Select The Personality'), ('Good Person', 'Good Person'), ('Inocent', 'Inocent'), ('Extrovert', 'Extrovert')], max_length=100, null=True)),
                ('salary', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('experience', models.BooleanField(null=True)),
                ('smoker', models.CharField(choices=[('1', 'YES'), ('2', 'NO')], default='', max_length=100, null=True)),
            ],
        ),
    ]