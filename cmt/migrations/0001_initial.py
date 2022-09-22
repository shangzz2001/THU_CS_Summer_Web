# Generated by Django 4.0.6 on 2022-09-04 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0004_articlepost_pre_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cmt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cmt', to='article.articlepost')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
