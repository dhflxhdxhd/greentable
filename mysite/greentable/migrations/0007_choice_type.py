# Generated by Django 3.2.3 on 2021-06-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greentable', '0006_choice_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='type',
            field=models.IntegerField(null=True),
        ),
    ]
