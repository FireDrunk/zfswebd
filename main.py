import os, sys
DIRNAME = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(DIRNAME)
sys.path.insert(0, ROOT)

import cherrypy




from pages.home import Home
root = Home()

from pages.disks import Disks
root.disks = Disks()

from pages.network import Network
root.network= Network()

from pages.zfs import ZFS
root.zfs = ZFS()

cherrypy.quickstart(root,'/','app.config')