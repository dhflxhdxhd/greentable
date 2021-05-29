# Generated by Django 3.2.3 on 2021-05-29 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20)),
                ('explain', models.IntegerField(blank=True)),
                ('division', models.IntegerField(blank=True)),
                ('country', models.IntegerField(blank=True)),
                ('call', models.CharField(blank=True, max_length=20)),
                ('locate', models.CharField(blank=True, max_length=50)),
                ('time', models.CharField(blank=True, max_length=100)),
                ('day_break', models.CharField(blank=True, max_length=30)),
                ('menu', models.CharField(blank=True, max_length=20)),
                ('etc', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
