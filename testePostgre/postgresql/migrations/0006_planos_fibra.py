# Generated by Django 5.0.6 on 2024-05-17 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgresql', '0005_planos_delete_combos_rename_empresas_provedor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='planos',
            name='fibra',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
