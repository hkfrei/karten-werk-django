# Generated by Django 4.1 on 2022-09-19 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kartenwerk', '0024_alter_referenz_titel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=100, verbose_name='Title')),
                ('kurzbeschrieb', models.TextField(verbose_name='Kurzbeschrieb')),
                ('datum', models.DateField(verbose_name='Publizierungsdatum')),
                ('teaser_img', models.CharField(max_length=100, verbose_name='Vorschaubild')),
                ('url', models.URLField(verbose_name='URL zum Post')),
                ('verfasser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kartenwerk.stakeholder')),
            ],
            options={
                'verbose_name_plural': 'Blogposts',
            },
        ),
    ]
