# Generated by Django 2.2.3 on 2019-07-09 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_auto_20190709_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to='movies_banner'),
            preserve_default=False,
        ),
    ]