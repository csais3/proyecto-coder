# Generated by Django 4.0.5 on 2022-07-01 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_rentakids', '0002_alter_cliente_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=255, verbose_name='Teléfono'),
        ),
    ]
