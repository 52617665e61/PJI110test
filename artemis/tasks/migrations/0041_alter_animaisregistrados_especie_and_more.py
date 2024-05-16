# Generated by Django 5.0.2 on 2024-05-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0040_delete_especie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaisregistrados',
            name='especie',
            field=models.CharField(choices=[('Cachorro', 'cachorro'), ('Cavalo', 'cavalo'), ('Gato', 'gato'), ('Periquito', 'periquito')], max_length=20),
        ),
        migrations.AlterField(
            model_name='animaisregistrados',
            name='raca',
            field=models.CharField(choices=[('Shih-Tzu', 'Shih-Tzu'), ('Buldogue Francês', 'Buldogue Francês'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Poodle', 'Poodle'), ('Maltês', 'Maltês'), ('Pug', 'Pug'), ('Sem raça definida', 'SRD')], max_length=20),
        ),
    ]