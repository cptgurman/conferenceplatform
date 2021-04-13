# Generated by Django 3.1.6 on 2021-03-26 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210325_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberapplication',
            name='expert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='expert', to='core.member', verbose_name='Эксперт'),
        ),
    ]