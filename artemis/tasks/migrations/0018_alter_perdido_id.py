# Generated by Django 5.0.2 on 2024-03-12 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_perdido_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perdido',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
