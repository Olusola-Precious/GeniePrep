# Generated by Django 3.1.4 on 2021-03-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='short_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subjects',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
