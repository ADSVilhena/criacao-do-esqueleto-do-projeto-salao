# Generated by Django 2.1.7 on 2019-04-01 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_reserva', models.DateField()),
                ('hora_reserva', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='cliente',
            name='pontos_cliente',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='pontos_produto',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='pontos_servico',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor_servico',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='reserva',
            name='cliente_reserva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salao.Cliente'),
        ),
    ]
