# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.CharField(default=b'2014', max_length=4, choices=[(b'2010', b'2010'), (b'2011', b'2011'), (b'2012', b'2012'), (b'2013', b'2013'), (b'2014', b'2014'), (b'2015', b'2015')]),
            preserve_default=True,
        ),
    ]
