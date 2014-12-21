# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.FileField(upload_to=b'static/upload/')),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('year', models.IntegerField(max_length=4, choices=[(b'2010', b'2010'), (b'2011', b'2011'), (b'2012', b'2012')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
