# Generated by Django 4.0.4 on 2022-07-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_app', '0003_remove_usuario_perfil_email_usuario_perfil_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario_perfil',
            name='descripcion',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]