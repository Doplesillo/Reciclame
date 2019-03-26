# Generated by Django 2.0.7 on 2019-03-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_historialcanje'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Pendiente', max_length=50)),
                ('descripcion', models.CharField(default=' ', max_length=50)),
                ('direccion', models.CharField(default=' ', max_length=100)),
                ('telefono', models.IntegerField(default=0)),
                ('horario', models.CharField(default=' ', max_length=25)),
                ('email', models.CharField(default=' ', max_length=50)),
                ('pagina', models.CharField(default=' ', max_length=80)),
                ('giro', models.CharField(default=' ', max_length=40)),
            ],
        ),
    ]