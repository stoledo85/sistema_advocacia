# Generated by Django 3.0.11 on 2020-11-25 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='dt_encerramento',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='dt_trans_julgado',
        ),
    ]
