# Generated by Django 4.0.6 on 2022-09-05 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_remove_articlepost_column_delete_articlecolumn'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='tag',
            field=models.CharField(default='None', max_length=10),
        ),
    ]
