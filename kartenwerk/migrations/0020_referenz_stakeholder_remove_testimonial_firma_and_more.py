# Generated by Django 4.1 on 2022-09-16 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kartenwerk', '0019_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referenz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(default='Title', max_length=100, verbose_name='Title')),
                ('kurzbeschrieb', models.TextField(default='Kurzbeschrieb', verbose_name='Kurzbeschrieb')),
                ('bild', models.CharField(max_length=50, verbose_name='Bild')),
                ('video', models.CharField(max_length=50, verbose_name='Video')),
                ('angebot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kartenwerk.angebot')),
            ],
            options={
                'verbose_name_plural': 'Referenzen',
            },
        ),
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=100, verbose_name='Logo')),
                ('firma', models.CharField(max_length=100, verbose_name='Titel')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('vorname', models.CharField(max_length=50, verbose_name='Vorname')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
            ],
            options={
                'verbose_name_plural': 'Stakeholders',
            },
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='firma',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='name',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='position',
        ),
        migrations.RemoveField(
            model_name='testimonial',
            name='vorname',
        ),
        migrations.DeleteModel(
            name='Angebotbeispiel',
        ),
        migrations.AddField(
            model_name='referenz',
            name='stakeholder',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='kartenwerk.stakeholder'),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='stakeholder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kartenwerk.stakeholder'),
        ),
    ]