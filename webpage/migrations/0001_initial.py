# Generated by Django 2.0.7 on 2018-11-13 17:40

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rol', models.CharField(choices=[('1', 'Usuario'), ('2', 'Centro'), ('3', 'Admin')], max_length=3)),
                ('puntos_totales', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Centro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('place_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cita', models.DateField()),
                ('num_residuos', models.IntegerField(default=1)),
                ('fecha_aprobacion', models.DateField(blank=True, default=None, null=True)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Centro')),
            ],
        ),
        migrations.CreateModel(
            name='LimitWaste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limit', models.IntegerField(default=0)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Centro')),
            ],
        ),
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('reward_points', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Punto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Residuo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_name', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ResiduoLugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limite', models.IntegerField()),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Centro')),
                ('residuo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Residuo')),
            ],
        ),
        migrations.AddField(
            model_name='punto',
            name='waste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Residuo'),
        ),
        migrations.AddField(
            model_name='limitwaste',
            name='waste',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Residuo'),
        ),
        migrations.AddField(
            model_name='cita',
            name='residuo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Residuo'),
        ),
        migrations.AddField(
            model_name='cita',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
