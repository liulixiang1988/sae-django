# -*- coding:utf-8 -*-
import sae
from liulixianglife import wsgi
from django.conf import settings
import os
import sys


#两者取其一

sys.path.insert(0, os.path.join(settings.BASE_DIR, 'site-packages'))
application = sae.create_wsgi_app(wsgi.application)