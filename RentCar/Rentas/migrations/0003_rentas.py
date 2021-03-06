# Generated by Django 3.2.6 on 2021-09-28 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Rentas', '0002_autos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rentas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_renta', models.DateField()),
                ('duracion_renta', models.IntegerField()),
                ('fecha_salida', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('autos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rentas.autos')),
                ('clientes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rentas.clientes')),
            ],
        ),
    ]
