# Generated by Django 3.2.6 on 2021-09-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rentas', '0003_rentas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='fechaNaci',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Nacimiento'),
        ),
    ]
