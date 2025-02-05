# Generated by Django 4.2.10 on 2024-05-30 16:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(verbose_name='投稿文')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]
