# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

	dependencies = [
		('api', '0004_auto_20150325_2339'),
	]

	operations = [
		migrations.AlterField(
			model_name='appuser',
			name='user',
			field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
			preserve_default=True,
		),
	]
