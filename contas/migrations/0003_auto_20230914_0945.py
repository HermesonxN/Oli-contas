# Generated by Django 3.2.21 on 2023-09-14 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_transacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transacoes'},
        ),
    ]