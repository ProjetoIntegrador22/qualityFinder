# Generated by Django 5.0.6 on 2024-05-13 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.DecimalField(decimal_places=0, max_digits=14)),
            ],
        ),
    ]
