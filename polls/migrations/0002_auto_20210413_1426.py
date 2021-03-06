# Generated by Django 3.1.6 on 2021-04-13 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NBAPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('jerseyNumber', models.IntegerField(default=0, max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='NBATeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(default='', max_length=70)),
                ('city', models.CharField(default='', max_length=50)),
                ('mascot', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favTeam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.nbateam')),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.AddField(
            model_name='nbaplayer',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.nbateam'),
        ),
    ]
