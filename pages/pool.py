from page import Page
import cherrypy

class Pool(Page):
    def default(self, poolname = None):
        if poolname is None:
            raise cherrypy.HTTPRedirect("/zfs")
        else:
            result = self.rpcclient.call("zfs", "get_pool_info", poolname)
            return self.env.get_template('zfs/pool/overview.html').render(name = poolname, content = result)
    default.exposed = True
