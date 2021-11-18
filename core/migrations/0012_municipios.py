# Generated by Django 3.2.6 on 2021-11-17 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_municipiobr_ibge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('ibge', models.CharField(max_length=200, null=True)),
                ('uf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.estado')),
            ],
        ),
    ]