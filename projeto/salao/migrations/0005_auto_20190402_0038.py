# Generated by Django 2.1.7 on 2019-04-02 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0004_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='data_hora_venda',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]