# Generated by Django 5.0.2 on 2024-05-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0037_especie_alter_animaisregistrados_especie_raca_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaisregistrados',
            name='especie',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='animaisregistrados',
            name='raca',
            field=models.CharField(max_length=20),
        ),
    ]
