# Generated by Django 4.2.6 on 2024-02-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_productcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='FlowType',
            field=models.CharField(choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')], max_length=50, verbose_name='Tipo de flujo'),
        ),
    ]
