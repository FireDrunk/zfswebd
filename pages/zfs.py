from page import Page
from pages.pool import Pool

class ZFS(Page):
    pool = Pool()

    def default(self):
        return self.overview()
    default.exposed = True

    def overview(self):
        fslist = self.rpcclient.call('zfs', 'list_filesystems')
        poollist = self.rpcclient.call('zfs', 'list_pools')
        return self.env.get_template('zfs/overview.html').render(fs = fslist, pl = poollist)
    overview.exposed = True


    pool.exposed = True

