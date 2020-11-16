"""
	Databases config
	Defined the databases that will be used in AccessorUnit's all django-app.
"""

import os
from AccessorUnit import settings as setting


class Database:
	DBs = {
		'default': {
	        'ENGINE': 'django.db.backends.sqlite3',
	        'NAME': 'sqlite',
		}
	}