# Generated by Django 3.0.5 on 2020-04-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_permissioncode'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(blank=True, choices=[(None, '-----'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default=None, max_length=1, null=True, verbose_name='Kjønn'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(blank=True, max_length=140, null=True, verbose_name='Avdeling'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Fornavn'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Etternavn'),
        ),
    ]
