import os, sys
DIRNAME = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(DIRNAME)
sys.path.insert(0, ROOT)

import cherrypy

class Root:pass
from pages.status import Status
root = Root()
root.status = Status()

from pages.disks import Disks
root.disks = Disks()

cherrypy.quickstart(root,'/','app.config')