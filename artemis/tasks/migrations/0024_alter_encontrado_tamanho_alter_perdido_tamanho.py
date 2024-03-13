# Generated by Django 5.0.2 on 2024-03-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0023_rename_fk_perdido_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encontrado',
            name='tamanho',
            field=models.CharField(choices=[('Pequeno', 'pequeno'), ('M', 'medio'), ('G', 'grande')], max_length=20),
        ),
        migrations.AlterField(
            model_name='perdido',
            name='tamanho',
            field=models.CharField(choices=[('Pequeno', 'pequeno'), ('M', 'medio'), ('G', 'grande')], max_length=20),
        ),
    ]
