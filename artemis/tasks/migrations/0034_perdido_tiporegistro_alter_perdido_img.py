# Generated by Django 5.0.2 on 2024-04-08 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0033_alter_perdido_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='perdido',
            name='tipoRegistro',
            field=models.CharField(default='Perdido', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perdido',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='animais/'),
        ),
    ]
