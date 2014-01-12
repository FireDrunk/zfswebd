from page import Page
class Disks(Page):
    def default(self, indentifier = None):
        return self.overview()
    default.exposed = True

    def overview(self, identifier = None):
        if identifier is None:
            diskList = self.rpcclient.call('disk', 'get_all')
            self.content = {'content' : diskList}
            return self.env.get_template('disks/overview.html').render(self.content)
        else:
            diskinfo = self.rpcclient.call('disk', 'get_info', identifier)
            self.content = {'content' : diskinfo}
            return self.env.get_template('disks/diskinfo.html').render(self.content)
    overview.exposed = True

    def health(self, identifier = None):
        if identifier is None:
            diskHealthList = self.rpcclient.call('disk', 'get_all_health')
            self.content = {'content' : diskHealthList}
            return self.env.get_template('disks/healthoverview.html').render(self.content)
        else:
            diskHealth= self.rpcclient.call('disk', 'get_health', identifier)
            self.content = {'content' : diskHealth}
            return self.env.get_template('disks/health.html').render(self.content)
    health.exposed = True

