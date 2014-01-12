from page import Page
class Disks(Page):
    def default(self):
        return self.overview()
    default.exposed = True

    def overview(self, identifier = None):
        if identifier is None:
            diskList = self.rpcclient.call('disk', 'get_all')
            self.content = {'content' : diskList}
            return self.env.get_template('disks/overview.html').render(self.content)
        else:
            diskinfo = self.rpcclient.call('disk', 'get_info')
            self.content = {'content' : diskinfo}
            return self.env.get_template('disk/diskinfo.html').render(self.content)
    overview.exposed = True

    def health(self, identifier = None):
        if identifier is None:
            diskHealthList = self.rpcclient.call('disk', 'get_all_health')
            self.content = {'content' : diskHealthList}
            return self.env.get_template('disks/smartoverview.html').render(self.content)
        else:
            diskHealth= self.rpcclient.call('disk', 'get_health')
            self.content = {'content' : diskHealth}
            return self.env.get_template('disk/smart.html').render(self.content)
    health.exposed = True

