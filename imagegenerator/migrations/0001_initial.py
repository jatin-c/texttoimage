# Generated by Django 5.1 on 2024-08-10 20:55

import imagegenerator.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=imagegenerator.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
