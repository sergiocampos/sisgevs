# Generated by Django 3.2.6 on 2021-10-27 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_joinmunicipioibgeunidadesaude'),
    ]

    operations = [
        migrations.RenameField(
            model_name='joinmunicipioibgeunidadesaude',
            old_name='ibge_id',
            new_name='ibge',
        ),
        migrations.RenameField(
            model_name='joinmunicipioibgeunidadesaude',
            old_name='municipio_id',
            new_name='municipio',
        ),
        migrations.RenameField(
            model_name='joinmunicipioibgeunidadesaude',
            old_name='unidade_saude_id',
            new_name='unidade_saude',
        ),
    ]
