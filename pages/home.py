from page import Page
import cherrypy

class Home(Page):
    def index(self):
        raise cherrypy.HTTPRedirect("/status")
    index.exposed = True

    def status(self):
        self.content = {'content' : 'Status'}
        return self.env.get_template('status/status.html').render(self.content)
    status.exposed = True

    def cpu(self):
        cpuinfo = self.rpcclient.call("status", "get_cpu_info")
        self.content = {
                        'machinetype' : cpuinfo['machine'],
                        'model' : cpuinfo['model'],
                        'cpucount' : cpuinfo['ncpu'],
                        'architecture' : cpuinfo['arch']}
        return self.env.get_template('status/cpu.html').render(self.content)
    cpu.exposed = True

    def memory(self):
        self.content = {'content' : 'Memory'}
        return self.env.get_template('status/memory.html').render(self.content)
    memory.exposed = True

    def logs(self):
        self.content = {'content' : 'Logs'}
        return self.env.get_template('status/logs.html').render(self.content)
    logs.exposed = True

    def release(self):
        self.content = {'content' : 'Release Info'}
        return self.env.get_template('status/release.html').render(self.content)
    release.exposed = True