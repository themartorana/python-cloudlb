# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"

USAGE = """usage: cloudlb [-u USERNAME] [-k API_KEY]
               [-l DATACENTER_LOCATION] COMMAND ARGS

cloudlb is a tool allowing to interface to Rackspace Cloud
Load-Balancer service.

COMMANDS:

  add
  create
  delete
  list
  set
  show

Add help to command like :

   cloudlb add help

to display help for the add command."""

HELP_SET = """usage: set [connection_logging|session_persistence|healthmonitor|loadbalancer|node]

- Set load balancer attributes :
Usage:
 cloudlb set loadbalancer LOADBALANCER_ID name=NEWNAME port=PORT
         protocol=(HTTP|FTP|HTTPS|POP.....)
         algorithm=(LEAST_CONNECTIONS|RANDOM|ROUND_ROBIN|
                    WEIGHTED_LEAST_CONNECTIONS|WEIGHTED_ROUND_ROBIN)
Example:
 cloudlb set loadbalancer LOADBALANCER_ID name=MyNewName1
         port=2021 protocol=FTP algorithm=ROUND_ROBIN
 cloudlb set loadbalancer LOADBALANCER_ID name=MyNewName1
         port=8043 protocol=HTTPS algorithm=RANDOM

- Set node attribute :
Usage:
 set node LOADBALANCER_ID NODE_ID condition=(ENABLED|DISABLED|DRAINING)
Example:
 cloudlb set node LOADBALANCER_ID NODE_ID condition=ENABLED

- Enable or Disable connection_logging :
Usage:
 set connection_logging LOADBALANCER_ID (ENABLE|DISABLE)
Example:
 cloudlb set connection_logging LOADBALANCER_ID enable

- Set session persistence on load balancer:
Usage:
  set session_persistence LOADBALANCER_ID HTTP_COOKIE
Example:
  cloudlb set session_persistence LOADBALANCER_ID HTTP_COOKIE

- Set health monitoring on load balancer :
Usage:
  set healthmonitor LOADBALANCER_ID type=(CONNECT|HTTP|HTTPS)
                       delay=SECONDS timeout=SECONDS
                       attemptsBeforeDeactivation=NUMBER
                       [ path=HTTP_PATH statusRegex=REGEXP
                         bodyRegex=REGEXP ]
Examples:
  cloudlb set healthmonitor LOADBALANCER_ID type="CONNECT"
          delay="10" timeout="10" attemptsBeforeDeactivation=4

  cloudlb set healthmonitor LOADBALANCER_ID type="HTTP" delay="5" timeout="2"
          attemptsBeforeDeactivation=3 path=/
          statusRegex="^[234][0-9][0-9]$" bodyRegex=testing
"""

HELP_ADD = """usage: add [access_list|node]

- Add network access list :
Usage:
  add access_list (ALLOW|DENY):NETWORK
Example:
  cloudlb add access_list LOADBALANCER_ID ALLOW:127.0.0.1/24

- Add node to a load balancer :
Usage:
 add node LOADBALANCER_ID condition="ENABLED|DISABLED|DRAINING"
          port=PORT address=IPV4_ADDRESS
Example:
  cloudlb add node LOADBALANCER_ID
          condition=ENABLED port=80 address=98.129.220.40
"""

HELP_SHOW = """
usage: show [limits|usage|algorithms|protocols|healthmonitor|
             session_persistence|connection_logging|loadbalancer|
             access_list|node|nodes]

- Show all load balancer limits :
Usage:
  show limits
Example:
  cloudlb show limits

- Show all (or specific) load balancer usage :
Usage:
  show usage [LOADBALANCER_ID]
Example:
  cloudlb show usage

- Show algorithms available :
Usage:
  show algorithms
Example:
  cloudlb show algorithms

- Show protocols available :
Usage:
  show protocols
Example:
  cloudlb show protocols

- Show Health Monitor type on LoadBalancer
Usage:
  show healthmonitor LOADBALANCER_ID
Example:
  cloudlb show healthmonitor LOADBALANCER_ID

- Show Session persistence type on LoadBalancer
Usage:
  show session_persistence LOADBALANCER_ID
Example:
  cloudlb show session_persistence LOADBALANCER_ID

- Show Connection type on LoadBalancer
Usage:
  show connection_logging LOADBALANCER_ID
Example:
  cloudlb show connection_logging LOADBALANCER_ID

- Show details about LoadBalancer
Usage:
  show loadbalancer LOADBALANCER_ID
Example:
  cloudlb show loadbalancer LOADBALANCER_ID

- Show access lists of LoadBalancer
Usage:
  show access_lists LOADBALANCER_ID
Example:
  cloudlb show access_lists LOADBALANCER_ID

- Show details about node.
Usage:
  show node LOADBALANCER_ID NODE_ID
Example:
  cloudlb show node LOADBALANCER_ID NODE_ID

"""

HELP_LIST = """usage: list [loadbalancers|nodes|access_lists]

- List loadbalancers
Usage:
  list loadbalancers [FILTER]
Filters:
  address
  id
  name
  port
  protocol
  status
Example:
  cloudlb list loadbalancers protocol=HTTP status=ENABLED

- List nodes of load balancers
Usage:
  list nodes LOADBALANCER_ID [FILTER]
Filters:
  address
  id
  port
  condition
  status
Example:
  cloudlb list nodes LOADBALANCER_ID port=80

- List access lists of load balancers
Usage:
  list access_lists LOADBALANCER_ID
Example:
  cloudlb list access_lists LOADBALANCER_ID
"""

HELP_DELETE = """usage: delete [loadbalancer|node|access_list|session_persistence|healthmonitor]

- Delete LoadBalancer :
Usage:
  delete loadbalancer LOADBALANCER_ID
Example:
  cloudlb delete loadbalancer LOADBALANCER_ID

- Delete node of LoadBalancer :
Usage:
  delete node LOADBALANCER_ID NODE_ID
Example:
  cloudlb delete node LOADBALANCER_ID NODE_ID

- Delete access_list of loadbalancer
Usage:
  delete access_list LOADBALANCER_ID (ACCESS_LIST_ID|all)
Example:
  cloudlb delete access_list all

- Delete session_persistence of loadbalancer
Usage:
  delete session_persistence LOADBALANCER_ID
Example:
  cloudlb delete session_persistence LOADBALANCER_ID

- Delete healthmonitor of loadbalancer
Usage:
  delete healthmonitor LOADBALANCER_ID
Example:
  cloudlb delete healthmonitor LOADBALANCER_ID


"""

HELP_CREATE = """
- Create LoadBalancer
Usage:
  create loadbalancer protocol=PROTOCOL name=NAME PORT=PORT \
         NODE1::address=IP_ADDRESS,port=PORT,condition=CONDITION \
         NODE2::address=IP_ADDRESS,port=PORT,condition=CONDITION \
         virtualIp1::type=PUBLIC

  Multiple nodes can be specified

Example:
create loadbalancer \
    protocol="HTTP" name=A_NAME port=80 \
    node1::address="100.1.0.1",port=80,condition=ENABLED \
    node2::address="100.1.0.2",port=80,condition=ENABLED \
    virtualIp1::type=PUBLIC

"""

EPILOG = ""
