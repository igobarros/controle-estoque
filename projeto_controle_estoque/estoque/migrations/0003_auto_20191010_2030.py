# Generated by Django 2.2.5 on 2019-10-10 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20190929_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='funcionario',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='estoque',
            name='movimento',
            field=models.CharField(blank=True, choices=[('e', 'entrada'), ('s', 'saida')], max_length=1),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='saldo',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
