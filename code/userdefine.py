#encoding=utf-8

from mininet.net import Mininet

net = Mininet()

#Creating nodes in the network
c0 = net.addController()
h0 = net.addHost('h0')
s0 = net.addSwitch('s0')
h1 = net.addHost('h1')

#Creating links between nodes in the network
net.addLink(h0, s0)
net.addLink(h1, s0)

#Configuration of IP address in interfaces
h0.setIP('192.168.1.1', 24)
h1.setIP('192.168.1.2', 24)

net.start()
net.pingAll()
net.stop()


