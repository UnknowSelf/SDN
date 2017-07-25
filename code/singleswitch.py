#encoding=utf-8

from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo

single3 = SingleSwitchTopo(k=3)     #一个交换机下挂3个主机
net = Mininet(topo=single3)

net.start()
net.pingAll()
net.stop()


