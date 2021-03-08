# Generated by Django 3.1.7 on 2021-03-08 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_auto_20210307_2027'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mis departamentos', 'verbose_name_plural': 'Areas de la empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'short_name')},
        ),
    ]
