# Generated by Django 5.0.2 on 2024-03-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontrado',
            name='cor',
            field=models.CharField(choices=[('Amarelo', 'Amarelo'), ('Azul', 'Azul'), ('Branco', 'Branco'), ('Marrom', 'Marrom'), ('Preto', 'Preto')], max_length=20),
        ),
        migrations.AlterField(
            model_name='encontrado',
            name='especie',
            field=models.CharField(choices=[('Cachorro', 'cachorro'), ('Cavalo', 'cavalo'), ('Gato', 'gato'), ('Periquito', 'periquito')], max_length=20),
        ),
        migrations.AlterField(
            model_name='encontrado',
            name='raca',
            field=models.CharField(choices=[('Shih-Tzu', 'Shih-Tzu'), ('Buldogue Francês', 'Buldogue Francês'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Poodle', 'Poodle'), ('Maltês', 'Maltês'), ('Pug', 'Pug'), ('Sem raça definida', 'SRD')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perdido',
            name='cor',
            field=models.CharField(choices=[('Amarelo', 'Amarelo'), ('Azul', 'Azul'), ('Branco', 'Branco'), ('Marrom', 'Marrom'), ('Preto', 'Preto')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perdido',
            name='especie',
            field=models.CharField(choices=[('Cachorro', 'cachorro'), ('Cavalo', 'cavalo'), ('Gato', 'gato'), ('Periquito', 'periquito')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perdido',
            name='raca',
            field=models.CharField(choices=[('Shih-Tzu', 'Shih-Tzu'), ('Buldogue Francês', 'Buldogue Francês'), ('Yorkshire Terrier', 'Yorkshire Terrier'), ('Poodle', 'Poodle'), ('Maltês', 'Maltês'), ('Pug', 'Pug'), ('Sem raça definida', 'SRD')], max_length=20),
        ),
    ]
