# Generated by Django 2.0.7 on 2019-03-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_partners_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partners',
            name='image',
            field=models.ImageField(default='example.jpg', upload_to='images/partners/'),
        ),
    ]
