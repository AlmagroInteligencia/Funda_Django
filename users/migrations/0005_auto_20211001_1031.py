# Generated by Django 3.2.6 on 2021-10-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cars',
            field=models.ManyToManyField(to='users.Car', verbose_name='los autos de la persona'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='el nombre de la persona'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='el apellido de la persona'),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
