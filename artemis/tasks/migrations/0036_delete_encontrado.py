# Generated by Django 5.0.2 on 2024-04-11 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0035_rename_perdido_animaisregistrados'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Encontrado',
        ),
    ]
