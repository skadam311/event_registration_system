# Generated by Django 2.0.5 on 2022-05-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0002_auto_20220527_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventlist',
            old_name='website',
            new_name='Website',
        ),
        migrations.AlterField(
            model_name='eventlist',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
