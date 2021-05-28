# Generated by Django 3.2.3 on 2021-05-26 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('explain', models.IntegerField()),
                ('division', models.IntegerField()),
                ('country', models.IntegerField()),
                ('call', models.CharField(max_length=20)),
                ('locate', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=100)),
                ('day_break', models.CharField(max_length=30)),
                ('menu', models.CharField(max_length=20)),
                ('etc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('place_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='greentable.place')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='greentable.question')),
            ],
        ),
    ]
