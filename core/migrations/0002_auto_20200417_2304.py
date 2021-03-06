# Generated by Django 3.0.5 on 2020-04-18 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author_comment',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
