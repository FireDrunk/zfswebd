from page import Page
class Network(Page):
    def default(self, indentifier = None):
        return self.overview()
    default.exposed = True

    def overview(self, identifier = None):
        if identifier is None:
            iflist = self.rpcclient.call('net', 'list_interfaces')
            resultlist = []
            for interface in iflist:
                ifinfo = self.rpcclient.call('net', 'get_address', interface)

                resultlist.append({
                                 'identifier' : interface,
                                 'addresses' : ifinfo,
                                 })
            return self.env.get_template('network/ifoverview.html').render(content = resultlist)
        else:
            rawifinfo = self.rpcclient.call('net', 'get_address', identifier)
            ifinfo = {
                      'identifier' : identifier,
                      'addresses' : rawifinfo
                      }
            return self.env.get_template('network/ifinfo.html').render(content = ifinfo)
    overview.exposed = True

    def firewall(self, identifier = None):
        return "TODO!"
    firewall.exposed = True

