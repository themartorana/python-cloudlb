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

  lbs = clb.loadbalancers.list()
  for lb in lbs:
      print "%s has %s node attached with IP addresses:" % (lb.name, len(lb.nodes))
      for ip in lb.virtualIps:
          print "%s/%s" % (ip.ipVersion, ip.address)

List deleted LoadBalancers::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")

  lbs = clb.loadbalancers.list_deleted()
  for x in lbs:
      print x.name


Get LB by ID::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  clb.authenticate()

  lb = clb.loadbalancers.get(LoadBalancerID)

Delete LB::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")

  lb = clb.loadbalancers.get(LoadBalancerID)
  lb.delete()

List nodes of a LB::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")

  lbs = clb.loadbalancers.list()
  lb = lbs[0] #get the first one
  nodes=lb.nodes.filter(status='ENABLED')
  for node in nodes:
      print node.address

Filter nodes via condition of a LB::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")

  lbs = clb.loadbalancers.list()
  lb = lbs[0] #get the first one
  for node in lb.nodes:
      print node.address

Add a node to a LB::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
 
  newnode =  cloudlb.Node(address="10.180.160.131",
                          port=80,
                          condition="ENABLED")

  lbs = clb.loadbalancers.list()
  lb = lbs[0] #add to the first one

  lb.add_nodes([newnode])
  

Delete a node from a LB::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
 
  lbs = clb.loadbalancers.list()
  lb = lbs[0] #add to the first one

  node = lb.nodes[0] #get the first node

  node.delete() #delete it

Update attributes of a node::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
 
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #add to the first one

  nodeid = 14106
  nodes = mylb.nodes  
  node = mylb.nodes.get(nodeid)
  toggle_status = node.condition == "ENABLED" and "DISABLED" or "ENABLED"
  node.condition = toggle_status
  node.update()

Get weight of a node by using .get()::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
 
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #add to the first one

  nodeid = 14106
  nodes = mylb.nodes  
  node = mylb.nodes.get(nodeid)
  print node.weight

Update attributes on LoadBalancer::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")

  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  mylb.protocol = "FTP"
  mylb.name = "APrettyNewName"

  mylb.update()

Get usage statitiscs on all LoadBalancers::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  print clb.get_usage()

Get usage statitiscs on a specfic LoadBalancer::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  print mylb.get_usage()

Get limits on all LoadBalancers::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  print clb.get_limits()

Get Load Balancing Algorithms::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  print clb.get_algorithms()

Get Load Balancing Protocols::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  print clb.get_protocols()

Get current Health Monitor::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  hm_monitor = mylb.healthmonitor()
  print hm_monitor.get()

Monitor loadbalancer using simple TCP Connect::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  hm_monitor = mylb.healthmonitor()
  hm = cloudlb.healthmonitor.HealthMonitor(
    type="CONNECT",
    delay=10,
    timeout=10,
    attemptsBeforeDeactivation=3)
  
  hm_monitor.add(hm)

Monitor loadbalancer using HTTP(s)::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  hm_monitor = mylb.healthmonitor()
  hm = cloudlb.healthmonitor.HealthMonitor(
      type="HTTP", #or HTTPS
      delay=10,
      timeout=10,
      attemptsBeforeDeactivation=3,
      path="/",
      statusRegex="^[234][0-9][0-9]$",
      bodyRegex="testing")
  hm_monitor.add(hm)

Delete Health Monitor rule::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  hm_monitor = mylb.healthmonitor()
  hm_monitor.delete()

Add http cookie session persistense::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  ss = cloudlb.sessionpersistense.SessionPersistense(persistenceType="HTTP_COOKIE")

  ssp = mylb.session_persistense()
  ssp.add(ss)

Get session persistence::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  ssp = mylb.session_persistense()
  print ssp.get()

Delete session persistense configuration::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb

  ssp = mylb.session_persistense()
  ssp.delete()

Enable/Disable Connection Logging::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb
  cl = mylb.connection_logging()
  
  #Get connection logging status
  print cl.get()

  #Enable connection logging
  cl.enable()
  
  #Disable connection logging
  cl.disable()

Access Lists::

  #!/usr/bin/python
  import cloudlb
  clb = cloudlb.CloudLoadBalancer("username", "apikey","chicago")
  
  lbs = clb.loadbalancers.list()
  mylb = lbs[0] #first lb
  accesslist = mylb.accesslist()

  networkItem1 = cloudlb.accesslist.NetworkItem(
      address="10.20.30.40", type="ALLOW")

  networkItem2 = cloudlb.accesslist.NetworkItem(
      address="0.0.0.0/0", type="DENY")
    
  # Allow only 10.20.30.40
  accesslist.add([networkItem1, networkItem2])

  # List accesslists
  print accesslist.list()

  # Delete all accesslist
  accesslist.delete()

  # Delete accesslist by ID
  accesslist.delete(id=62)  


LICENSE
=======

See COPYING for license information. Copyright © 2011, Rackspace US, Inc.

Author
======

Chmouel Boudjnah <chmouel@chmouel.com>

