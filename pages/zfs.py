from page import Page
class ZFS(Page):
    def default(self, indentifier = None):
        return self.overview()
    default.exposed = True

    def overview(self):
        fslist = self.rpcclient.call('zfs', 'list_filesystems')
        poollist = self.rpcclient.call('zfs', 'list_pools')
        return self.env.get_template('zfs/overview.html').render(fs = fslist, pl = poollist)
    overview.exposed = True

