import xmlrpclib

class RpcClient():
    def __init__(self, server_url):
        self.server = xmlrpclib.Server(server_url)
    def call(self, package, method):
        return getattr(getattr(self.server, package), method)()