# Generated by Django 5.0 on 2024-08-09 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("saude", "0009_alter_denuncia_horariofuncionamento"),
    ]

    operations = [
        migrations.AlterField(
            model_name="denuncia",
            name="horaDaDenuncia",
            field=models.TimeField(),
        ),
    ]
