# Generated by Django 4.1.2 on 2023-01-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post_id',
            field=models.CharField(max_length=100),
        ),
    ]
