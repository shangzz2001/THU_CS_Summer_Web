# Generated by Django 4.0.6 on 2022-09-05 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_articlecolumn'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepost',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='article.articlecolumn'),
        ),
    ]
