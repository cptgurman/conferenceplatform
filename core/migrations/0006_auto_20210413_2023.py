# Generated by Django 3.1.7 on 2021-04-13 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210326_2057'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='memberapplication',
            unique_together={('member', 'conference_id')},
        ),
    ]
