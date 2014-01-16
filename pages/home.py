from page import Page
import cherrypy

class Home(Page):
    def index(self):
        raise cherrypy.HTTPRedirect("/status")
    index.exposed = True