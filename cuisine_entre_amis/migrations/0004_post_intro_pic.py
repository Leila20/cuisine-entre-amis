# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-03 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine_entre_amis', '0003_post_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='intro_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
