# Generated by Django 3.1.7 on 2021-03-25 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210325_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expertarticle',
            name='expert',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.member', verbose_name='Эксперт'),
        ),
    ]
