# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='zipcode',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
