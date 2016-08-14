# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 14:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0003_auto_20160730_1405'),
        ('user_stories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iteration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('duration', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
                ('user_story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_stories.UserStory')),
            ],
        ),
    ]
