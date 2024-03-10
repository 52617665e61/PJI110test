# Generated by Django 5.0.2 on 2024-03-09 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_perdido_adicional_perdido_fk_alter_perdido_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perdido',
            name='especie',
            field=models.CharField(choices=[('Cachorro', 'cachorro'), ('Cavalo', 'cavalo'), ('Gato', 'gato'), ('Periquito', 'periquito')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perdido',
            name='tempo',
            field=models.DateTimeField(),
        ),
    ]
