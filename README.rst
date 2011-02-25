==================================================================
 Python interface to Rackspace Load Balancer as a Service product
==================================================================

:Homepage:  https://github.com/chmouel/python-cloudlb
:Credits:   Copyright 2011 Chmouel Boudjnah <chmouel@chmouel.com>
:Licence:   BSD


Usage
=====

Not much documentation at the moment but just some quick typical usage
scripts you can do with this library. This is based on the latest version from :

http://docs.rackspacecloud.com/loadbalancers/api/clb-devguide-latest.pdf

Create a LoadBalancer::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  clb.authenticate()

  node1 = cloudlb.Node(address="10.180.160.131",
                       port=80,
                       condition="ENABLED")


  virtualIP1 = cloudlb.VirtualIP(
                   type="PUBLIC") 

  clb.loadbalancers.create(name="mytestinglb",
                           port=80,
                           protocol="HTTP",
                           nodes=[node1],
                           virtualIps=[virtualIp1])
  

List LoadBalancers::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  clb.authenticate()

  lbs = clb.loadbalancers.list()
  for lb in lbs:
      print "%s has %s node attached with IP addresses:" % (lb.name, len(lb.nodes))
      for ip in lb.virtualIps:
          print "%s/%s" % (ip.ipVersion, ip.address)

Get LoadBalancer by ID::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  clb.authenticate()

  lb = clb.loadbalancers.get(LoadBalancerID)

Delete LoadBalancer::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  clb.authenticate()

  lb = clb.loadbalancers.get(LoadBalancerID)
  lb.delete()

List deleted LoadBalancers::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  clb.authenticate()

  lbs = clb.loadbalancers.list_deleted()
  for x in lbs:
      print x.name
