# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savethedate', '0006_auto_20170228_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='conferma_inviata',
            field=models.BooleanField(default=False),
        ),
    ]
