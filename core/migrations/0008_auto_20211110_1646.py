# Generated by Django 3.2.6 on 2021-11-10 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20211104_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casoesporotricose',
            old_name='cantao_sus_paciente',
            new_name='cartao_sus_paciente',
        ),
        migrations.RenameField(
            model_name='casoesporotricose',
            old_name='data_exame1',
            new_name='data_resultado_exame1',
        ),
        migrations.RenameField(
            model_name='casoesporotricose',
            old_name='data_exame2',
            new_name='data_resultado_exame2',
        ),
        migrations.RenameField(
            model_name='casoesporotricose',
            old_name='data_exame3',
            new_name='data_resultado_exame3',
        ),
    ]
