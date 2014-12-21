# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20141220_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='year',
            field=models.IntegerField(max_length=4, choices=[(b'2010', 2010), (b'2011', 2011), (b'2012', 2012), (b'2013', 2013), (b'2014', 2014), (b'2015', 2015)]),
            preserve_default=True,
        ),
    ]
