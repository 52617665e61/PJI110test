# Generated by Django 5.0.2 on 2024-04-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0027_alter_perdido_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perdido',
            name='usuario',
            field=models.CharField(max_length=30),
        ),
    ]