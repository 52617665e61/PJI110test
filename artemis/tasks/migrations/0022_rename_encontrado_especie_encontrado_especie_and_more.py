# Generated by Django 5.0.2 on 2024-03-12 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_rename_especie_encontrado_encontrado_especie_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encontrado',
            old_name='encontrado_especie',
            new_name='especie',
        ),
        migrations.RenameField(
            model_name='encontrado',
            old_name='encontrado_raca',
            new_name='raca',
        ),
        migrations.RenameField(
            model_name='perdido',
            old_name='perdido_especie',
            new_name='especie',
        ),
        migrations.RenameField(
            model_name='perdido',
            old_name='perdido_raca',
            new_name='raca',
        ),
    ]
