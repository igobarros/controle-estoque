# Generated by Django 2.2.5 on 2019-10-10 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ('categoria',),
            },
        ),
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='produto.Categoria'),
        ),
    ]
