# Generated by Django 4.0.6 on 2022-09-05 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_alter_articlepost_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='abs',
            field=models.CharField(default='Empty', max_length=50),
        ),
    ]
