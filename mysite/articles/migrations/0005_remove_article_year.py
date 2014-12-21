# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20141220_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='year',
        ),
    ]
