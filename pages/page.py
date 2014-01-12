from rpcclient import RpcClient
from jinja2 import Environment, PackageLoader

class Page(object):
    def __init__(self):
        self.rpcclient = RpcClient('http://192.168.1.10:9090')
        self.env = Environment(loader=PackageLoader('zfswebd', 'templates'))
        return