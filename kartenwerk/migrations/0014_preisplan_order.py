# Generated by Django 4.1 on 2022-09-15 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartenwerk', '0013_remove_preisplan_titel_preisplan_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='preisplan',
            name='order',
            field=models.IntegerField(default=1, verbose_name='Order'),
        ),
    ]