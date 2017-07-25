#encoding=utf-8

#addHost()语法可以对主机cpu进行设置，以百分数的形式；addLink()语法可以设置带宽bw、延迟delay、最大队列的大小max_queue_size、损耗率loss

from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink

net = Mininet(host=CPULimitedHost, link=TCLink)

c0 = net.addController()
s0 = net.addSwitch('s0')

h0 = net.addHost('h0')
h1 = net.addHost('h1', cpu=0.5)
h2 = net.addHost('h2', cpu=0.5)

net.addLink(s0, h0, bw=10, delay='5ms', max_queue_size=1000, loss=10, use_htb=True)
net.addLink(s0, h1)
net.addLink(s0, h2)

net.start()
net.pingAll()
net.stop()
