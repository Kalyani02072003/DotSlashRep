# Generated by Django 3.2.10 on 2022-01-08 04:15

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('updated_on', models.DateField(auto_now=True)),
                ('important', models.BooleanField(default=False)),
                ('notes', tinymce.models.HTMLField()),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='title', unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
