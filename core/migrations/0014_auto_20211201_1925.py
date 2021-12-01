# Generated by Django 3.2.6 on 2021-12-01 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_merge_0011_auto_20211118_1316_0012_municipios'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casoesporotricose',
            old_name='data_coleta',
            new_name='data_coleta1',
        ),
        migrations.AddField(
            model_name='casoesporotricose',
            name='data_coleta2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='casoesporotricose',
            name='data_coleta3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='casoesporotricose',
            name='local_lesao_outro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='casoesporotricose',
            name='natureza_lesao_outro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='casoesporotricose',
            name='numero_gal1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='casoesporotricose',
            name='numero_gal2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='casoesporotricose',
            name='numero_gal3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='casoesporotricose',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='codigoibge',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='distrito',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='estado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gerencia',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='joindistritomunicipioibgeestado',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='joinmunicipioibgeunidadesaude',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='macrorregiao',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='municipio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='municipiobr',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='regiao',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='unidadesaude',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
