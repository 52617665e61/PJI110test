# Generated by Django 5.0.2 on 2024-04-08 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0034_perdido_tiporegistro_alter_perdido_img'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Perdido',
            new_name='AnimaisRegistrados',
        ),
    ]