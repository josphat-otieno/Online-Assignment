# Generated by Django 3.2.5 on 2021-07-28 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
