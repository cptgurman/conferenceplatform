# Generated by Django 3.1.7 on 2021-04-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210413_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberapplication',
            name='speech_file',
            field=models.FileField(blank=True, upload_to='', verbose_name='Файл'),
        ),
        migrations.AlterUniqueTogether(
            name='memberapplication',
            unique_together={('member', 'member_section')},
        ),
    ]
