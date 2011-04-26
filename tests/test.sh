#!/bin/bash
#TODO: Add wait connection feature.
cd $(python -c 'import os,sys;print os.path.dirname(os.path.dirname(os.path.realpath(sys.argv[1])))'  $0)

A="python bin/cloudlb"
LBNAME="unitTestClb"
set -e
set -x

### Create
${A} create loadbalancer \
    protocol="HTTP" name=$LBNAME port=80 \
    node1::address="10.180.160.131",port=80,condition=ENABLED \
    node2::address="10.180.160.130",port=80,condition=ENABLED \
    virtualIp1::type=PUBLIC

### Lists
# List all LoadBalancers
$A list loadbalancers >/dev/null

# List all deleted Loadbalancers
$A list loadbalancers deleted >/dev/null

# List filtering by 
LBTEST=$(${A} list loadbalancers name=$LBNAME|head -1|sed 's/ID: //;s/,.*//')

# List all nodes of a LoadBalancer (you can add filters as well see below)
$A list nodes ${LBTEST} >/dev/null

### SHOWS

# Show usage of all LB
$A show usage >/dev/null

# Show usage of specific LB
$A show usage ${LBTEST} >/dev/null

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
$A -w set connection_logging ${LBTEST} 0 >/dev/null
# Enable connection logging.
$A -w set connection_logging ${LBTEST} 1 >/dev/null
# Enable connection logging.
$A -w set connection_logging ${LBTEST} enable >/dev/null
# Disable connection logging.
$A -w set connection_logging ${LBTEST} disable >/dev/null
### ACCESS_LISTS

# Add an Access List
$A -w add access_list ${LBTEST} ALLOW:127.0.0.1/24 >/dev/null

# List access_list
LAST_ID=$($A -w list access_lists ${LBTEST} | tail -1 | sed 's/.*ID: //')

# Delete access List by id
$A -w delete access_list ${LBTEST} ${LAST_ID}  >/dev/null

# Add an access_list
$A -w add access_list ${LBTEST} ALLOW:127.0.0.1/24 >/dev/null

# Delete all access_lists
$A -w delete access_list ${LBTEST} all >/dev/null

### Session Persistence

# Set session_persistence to HTTP_COOKIE
$A -w set session_persistence ${LBTEST} HTTP_COOKIE >/dev/null

# Show session_persistence
$A -w show session_persistence ${LBTEST} >/dev/null

# Delete session_persistence
$A -w delete session_persistence ${LBTEST} >/dev/null

### Health Monitoring

# Set healthmonitor to CONNECT
$A -w set healthmonitor ${LBTEST} type="CONNECT" delay="10" timeout="10" attemptsBeforeDeactivation=4 >/dev/null

# Set healthmonitor to HTTP (need to have path statusRegex and bodyRegex)
$A -w set healthmonitor ${LBTEST} type="HTTP" delay="5" timeout="2" attemptsBeforeDeactivation=3 path=/ statusRegex="^[234][0-9][0-9]$" bodyRegex=testing >/dev/null

# Set healthmonitor to HTTPS (need to have path statusRegex and bodyRegex)
# $A -w set healthmonitor ${LBTEST} type="HTTPS" delay="5" timeout="1" attemptsBeforeDeactivation=5 path=/ statusRegex="^[234][0-9][0-9]$" bodyRegex=foobar >/dev/null

# Show healthmonitoring rule.
$A -w show healthmonitor ${LBTEST} >/dev/null

# Delete healthmonitorring
$A -w delete healthmonitor ${LBTEST} >/dev/null

### LoadBalancer attribute

# Update LoadBalancer attribute (1)
$A -w set loadbalancer ${LBTEST} name=UnitTest2 port=81 protocol=FTP algorithm=ROUND_ROBIN

# Update LoadBalancer attribute (2)
$A -w set loadbalancer ${LBTEST} name=UnitTest1 port=80 protocol=HTTP algorithm=RANDOM

### Nodes

# Add node
$A -w add node ${LBTEST} condition=ENABLED port=80 address=98.129.220.40

# List node filtering by address
NODEID=$($A -w list nodes ${LBTEST} address=98.129.220.40|sed 's/.*ID: \([0-9]*\).*/\1/')
echo ${NODEID}

# Show node detail
$A -w show node ${LBTEST} ${NODEID} >/dev/null

# Update Node attribute (1)
$A -w set node ${LBTEST} ${NODEID}  condition=DRAINING

# Update Node attribute (2)
$A -w set node ${LBTEST} ${NODEID}  condition=ENABLED

# Delete node by ID
$A -w delete node ${LBTEST} ${NODEID}

### Finish

# delete loadBalancer
${A} -w delete loadbalancer ${LBTEST}
