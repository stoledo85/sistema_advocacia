# Generated by Django 3.1.1 on 2021-02-10 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20201125_1729'),
        ('processos', '0003_auto_20201127_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Cliente'),
        ),
    ]
