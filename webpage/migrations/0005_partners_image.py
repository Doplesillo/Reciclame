# Generated by Django 2.0.7 on 2019-03-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0004_partners'),
    ]

    operations = [
        migrations.AddField(
            model_name='partners',
            name='image',
            field=models.ImageField(default='example.jpg', upload_to='images/partners'),
        ),
    ]