#encoding=utf-8

from mininet.net import Mininet
from mininet.topolib import TreeTopo

tree22 = TreeTopo(depth=2, fanout=2)     #树状拓扑，深度2,扇出2
net = Mininet(topo=tree22)

net.start()
net.pingAll()
net.stop()


