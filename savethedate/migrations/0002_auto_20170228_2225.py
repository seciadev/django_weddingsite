# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savethedate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='after_confirmed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='dinner_confirmed',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='full_day',
        ),
    ]
