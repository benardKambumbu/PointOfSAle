# Generated by Django 3.2 on 2021-11-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_checkedout_transactions'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkedout',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
    ]
