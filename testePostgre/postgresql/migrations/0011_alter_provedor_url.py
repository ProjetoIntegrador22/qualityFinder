# Generated by Django 5.0.6 on 2024-05-17 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postgresql', '0010_provedor_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provedor',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
