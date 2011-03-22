#!/bin/bash
#TODO: Add wait connection feature.
cd $(python -c 'import os,sys;print os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[1])))'  $0)

A="python bin/cloudlb -u $US_RCLOUD_USER -k $US_RCLOUD_KEY -l $US_RCLOUD_DATACENTER"
LBTEST=4256
set -e
set -x

#TODO: create loadBalancer
#TODO-TEST: delete loadbalancerId

### Create
${A} create loadbalancer \
    protocol="HTTP" name="unitTest1" port=80 \
    node1::address="10.180.160.131",port=80,condition=ENABLED \
    node2::address="10.180.160.130",port=80,condition=ENABLED \
    virtualIp1::type=PUBLIC name="foo11"

### Lists
# List all LoadBalancers
$A list loadbalancers >/dev/null

# List all deleted Loadbalancers
$A list loadbalancers deleted >/dev/null

# List all nodes of a LoadBalancer (you can add filters as well see below)
$A list nodes ${LBTEST} >/dev/null

### SHOWS

# Show usage of all LB
$A show usage >/dev/null

# Show usage of specific LB
$A show usage ${LBTEST} >/dev/null

# Show Limits
$A show limits >/dev/null  || true # TODO: Sometime work sometime don't

# Show algorithms available
$A show algorithms >/dev/null

# Show protocols available
$A show protocols >/dev/null

# Show connection logging
$A show connection_logging ${LBTEST} >/dev/null

# Show details about loadbalancers
$A show loadbalancer ${LBTEST} >/dev/null

### Connection Logging

# Disable connection logging.
$A set connection_logging ${LBTEST} 0 >/dev/null
sleep 5
# Enable connection logging.
$A set connection_logging ${LBTEST} 1 >/dev/null
sleep 5
# Enable connection logging.
$A set connection_logging ${LBTEST} enable >/dev/null
sleep 5
# Disable connection logging.
$A set connection_logging ${LBTEST} disable >/dev/null
sleep 5
### ACCESS_LISTS

# Add an Access List
$A add access_list ${LBTEST} ALLOW:127.0.0.1/24 >/dev/null
sleep 5

# List access_list
LAST_ID=$($A list access_lists ${LBTEST} | tail -1 | sed 's/.*ID: //')
sleep 5

# Delete access List by id
$A delete access_list ${LBTEST} ${LAST_ID}  >/dev/null
sleep 5

# Add an access_list
$A add access_list ${LBTEST} ALLOW:127.0.0.1/24 >/dev/null
sleep 5

# Delete all access_lists
$A delete access_list ${LBTEST} all >/dev/null
sleep 2

### Session Persistence

# Set session_persistence to HTTP_COOKIE
$A set session_persistence ${LBTEST} HTTP_COOKIE >/dev/null
sleep 2

# Show session_persistence
$A show session_persistence ${LBTEST} >/dev/null
sleep 2

# Delete session_persistence
$A delete session_persistence ${LBTEST} >/dev/null
sleep 2

### Health Monitoring

# Set healthmonitor to CONNECT
$A set healthmonitor ${LBTEST} type="CONNECT" delay="10" timeout="10" attemptsBeforeDeactivation=4 >/dev/null
sleep 5

# Set healthmonitor to HTTP (need to have path statusRegex and bodyRegex)
$A set healthmonitor ${LBTEST} type="HTTP" delay="5" timeout="2" attemptsBeforeDeactivation=3 path=/ statusRegex="^[234][0-9][0-9]$" bodyRegex=testing >/dev/null
sleep 5

# Set healthmonitor to HTTPS (need to have path statusRegex and bodyRegex)
$A set healthmonitor ${LBTEST} type="HTTPS" delay="5" timeout="1" attemptsBeforeDeactivation=5 path=/ statusRegex="^[234][0-9][0-9]$" bodyRegex=foobar >/dev/null
sleep 5

# Show healthmonitoring rule.
$A show healthmonitor ${LBTEST} >/dev/null

# Delete healthmonitorring
$A delete healthmonitor ${LBTEST} >/dev/null
sleep 5

### LoadBalancer attribute

# Update LoadBalancer attribute (1)
$A set loadbalancer ${LBTEST} name=UnitTest2 port=81 protocol=FTP algorithm=ROUND_ROBIN
sleep 5

# Update LoadBalancer attribute (2)
$A set loadbalancer ${LBTEST} name=UnitTest1 port=80 protocol=HTTP algorithm=RANDOM
sleep 5

### Nodes

# Add node
$A add node ${LBTEST} condition=ENABLED port=80 address=98.129.220.40

# List node filtering by address
NODEID=$($A list nodes ${LBTEST} address=98.129.220.40|sed 's/.*ID: \([0-9]*\).*/\1/')
echo ${NODEID}

# Show node detail
$A show node ${LBTEST} ${NODEID} >/dev/null

# Update Node attribute (1)
$A set node ${LBTEST} ${NODEID}  condition=DRAINING
sleep 5

# Update Node attribute (2)
$A set node ${LBTEST} ${NODEID}  condition=ENABLED
sleep 5

# Delete node by ID
$A delete node ${LBTEST} ${NODEID}
