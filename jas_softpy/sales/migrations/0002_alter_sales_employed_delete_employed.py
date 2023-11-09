# Generated by Django 4.2.6 on 2023-11-09 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Postulation', '__first__'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='Employed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Postulation.employed'),
        ),
        migrations.DeleteModel(
            name='Employed',
        ),
    ]
