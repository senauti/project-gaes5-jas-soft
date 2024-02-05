# Generated by Django 4.2.6 on 2024-02-04 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Nombre')),
                ('position', models.CharField(max_length=55, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'empleado',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Postulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startOffers', models.DateTimeField(verbose_name='Fecha de la oferta')),
                ('descripOffer', models.TextField(max_length=250, verbose_name='Descripción de la Oferta')),
                ('profilePostulation', models.CharField(max_length=250, verbose_name='Perfil postulación')),
                ('StatePostulations', models.CharField(max_length=50, verbose_name='Estado Postulaciones')),
            ],
            options={
                'verbose_name': 'Postulación',
                'verbose_name_plural': 'Postulaciones',
                'db_table': 'postulacion',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Scheduling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateInterview', models.DateTimeField(verbose_name='Fecha de la entrevista agendamiento')),
                ('postulation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postulation.postulation')),
            ],
            options={
                'verbose_name': 'Agendamiento',
                'verbose_name_plural': 'Agentamientos',
                'db_table': 'agendamiento',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contractdate', models.DateField(verbose_name='Fecha del Contrato')),
                ('TypeContract', models.CharField(max_length=50, verbose_name='Tipo de Contrato')),
                ('Employed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='postulation.employed', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
                'db_table': 'contrato',
                'ordering': ['id'],
            },
        ),
    ]
