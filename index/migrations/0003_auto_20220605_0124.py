# Generated by Django 3.2.11 on 2022-06-04 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_performer_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='program',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
