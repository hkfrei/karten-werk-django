# Generated by Django 4.1 on 2022-09-15 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartenwerk', '0008_rename_bildname_angebotbeispiel_bild'),
    ]

    operations = [
        migrations.AddField(
            model_name='angebot',
            name='angebot_cards_beschrieb',
            field=models.TextField(default='Angebot Cards Beschrieb', verbose_name='Angebot Cards Beschrieb'),
        ),
        migrations.AddField(
            model_name='angebot',
            name='angebot_cards_titel',
            field=models.CharField(default='Angebot Cards Titel', max_length=100, verbose_name='Angebot Cards Titel'),
        ),
    ]