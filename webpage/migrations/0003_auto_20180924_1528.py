# Generated by Django 2.0.7 on 2018-09-24 15:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0002_premio'),
    ]

    operations = [
        migrations.AddField(
            model_name='premio',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='premio',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]