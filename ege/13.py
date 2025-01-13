from ipaddress import *

for mask in range(33):
    net = ip_network(f"117.191.37.84/{mask}",0)
    print(net, net.netmask)
