# Generated by Django 5.0.2 on 2024-04-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0032_alter_perdido_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perdido',
            name='img',
            field=models.ImageField(null=True, upload_to='animais/'),
        ),
    ]
