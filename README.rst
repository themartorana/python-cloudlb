==================================================================
 Python interface to Rackspace Load Balancer as a Service product
==================================================================

:Homepage:  https://github.com/chmouel/python-cloudlb
:Credits:   Copyright 2011 Chmouel Boudjnah <chmouel@chmouel.com>
:Licence:   BSD

Test
====

CREATE::
  import cloudlb

  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")

  clb.authenticate()

  node1 = cloudlb.Node(address="10.180.160.131",
                       port=80,
                       condition="ENABLED")


  virtualIP1 = cloudlb.VirtualIP(
                   type="PUBLIC") 

  for x in clb.loadbalancers.list():
      print "%s has %s node attached" % (x.name, len(x.nodes))
