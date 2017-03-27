# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savethedate', '0002_auto_20170228_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='after_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='dinner_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_day',
            field=models.BooleanField(default=True),
        ),
    ]
