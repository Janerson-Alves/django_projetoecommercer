# Generated by Django 4.1.1 on 2022-10-11 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
