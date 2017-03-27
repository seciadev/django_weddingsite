# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('savethedate', '0005_auto_20170228_2322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='after_confirmed',
            new_name='conferma_pranzo',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='dinner_confirmed',
            new_name='conferma_sera',
        ),
    ]
