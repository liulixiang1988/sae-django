# -*- coding:utf-8 -*-
import sae
import sys
import os
root = os.path.dirname(__file__)
# 如果是压缩包，就改为：site-packages.zip
sys.path.insert(0, os.path.join(root, 'site-packages'))

from liulixianglife import wsgi
application = sae.create_wsgi_app(wsgi.application)