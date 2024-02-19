# Generated by Django 4.2.6 on 2024-02-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('mobiliario', 'Mobiliario'), ('violencia_laboral', 'Violencia Laboral'), ('acoso_laboral', 'Acoso Laboral'), ('festividades', 'Festividades')], max_length=50, verbose_name='Categoría')),
                ('descriptCategory', models.CharField(max_length=50, verbose_name='Descripción de la Categoría')),
            ],
            options={
                'verbose_name': 'Sugerencia',
                'verbose_name_plural': 'Sugerencias',
                'db_table': 'buzonsugerencias',
                'ordering': ['id'],
            },
        ),
    ]
