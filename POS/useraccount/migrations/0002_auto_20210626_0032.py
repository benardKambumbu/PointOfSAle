# Generated by Django 3.1.5 on 2021-06-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bkuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
