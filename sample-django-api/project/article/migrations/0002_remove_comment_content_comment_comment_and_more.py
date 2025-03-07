# Generated by Django 5.1.6 on 2025-03-07 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='content',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article'),
        ),
    ]
