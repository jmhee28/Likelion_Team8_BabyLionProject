# Generated by Django 3.2.13 on 2022-06-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_alter_individual_info_posting_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individual_info',
            name='posting_num',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]