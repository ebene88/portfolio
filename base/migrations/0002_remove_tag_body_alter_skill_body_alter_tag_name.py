# Generated by Django 4.0.2 on 2022-03-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='body',
        ),
        migrations.AlterField(
            model_name='skill',
            name='body',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
