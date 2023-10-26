# Generated by Django 4.2.6 on 2023-10-26 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sigla_estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('endereco', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=40)),
                ('data_de_nascimento', models.CharField(max_length=60)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manter_alunos.cidade')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manter_alunos.curso')),
            ],
        ),
    ]
