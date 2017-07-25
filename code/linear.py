#encoding=utf-8

from mininet.net import Mininet
from mininet.topo import LinearTopo

Linear4 = LinearTopo(k=4)    #四个交换机分别下挂一个主机
net = Mininet(topo=Linear4)

net.start()
net.pingAll()
net.stop()


