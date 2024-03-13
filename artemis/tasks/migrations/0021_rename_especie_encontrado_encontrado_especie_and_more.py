# Generated by Django 5.0.2 on 2024-03-12 20:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0020_perdido_fk'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='encontrado',
            old_name='especie',
            new_name='encontrado_especie',
        ),
        migrations.RenameField(
            model_name='encontrado',
            old_name='raca',
            new_name='encontrado_raca',
        ),
        migrations.RenameField(
            model_name='perdido',
            old_name='especie',
            new_name='perdido_especie',
        ),
        migrations.RenameField(
            model_name='perdido',
            old_name='raca',
            new_name='perdido_raca',
        ),
        migrations.RemoveField(
            model_name='encontrado',
            name='caracteristica',
        ),
        migrations.AddField(
            model_name='encontrado',
            name='adicional',
            field=models.CharField(max_length=300, null=True, verbose_name='Informações adicionais'),
        ),
        migrations.AddField(
            model_name='encontrado',
            name='fk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='encontrado',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='encontrado',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='animais/'),
        ),
        migrations.AlterField(
            model_name='encontrado',
            name='tempo',
            field=models.DateField(),
        ),
    ]