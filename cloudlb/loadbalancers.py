# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb import base
from cloudlb.consts import LB_PROTOCOLS
from cloudlb.errors import InvalidProtocol, InvalidLoadBalancerName
from cloudlb.node import Node, NodeDict
from cloudlb.virtualip import VirtualIP


class LoadBalancer(base.Resource):
    def __repr__(self):
        return "<LoadBalancer: %s>" % self.name

    def delete(self):
        """
        Delete Load Balancer..
        """
        self.manager.delete(self)

    def _add_details(self, info):
        for (k, v) in info.iteritems():
            if k == "nodes":
                v = NodeDict([Node(parent=self, **x) for x in v])

            if k == "virtualIps":
                v = [VirtualIP(parent=self, **x) for x in v]

            if k in ('created', 'updated'):
                v['time'] = base.convert_time(v['time'])

            setattr(self, k, v)

    def add_nodes(self, nodes):
        self.manager.add_nodes(self.id, nodes)


class LoadBalancerManager(base.ManagerWithFind):
    resource_class = LoadBalancer

    def get(self, loadbalancerid):
        """
        Get a Load Balancer.

        :param loadbalancerid: ID of the :class:`LoadBalancer` to get.
        :rtype: :class:`LoadBalancer`
        """
        return self._get("/loadbalancers/%s.json" % \
                      base.getid(loadbalancerid), "loadBalancer")

    def list(self):
        """
        Get a list of loadbalancers.
        :rtype: list of :class:`LoadBalancer`

        Arguments:
        """
        return [x for x in \
                    self._list("/loadbalancers.json", "loadBalancers") \
                 if x._info['status'] != "DELETED"]

    def list_deleted(self):
        """
        Get a list of deleted loadbalancers.
        :rtype: list of :class:`LoadBalancer`

        Arguments:
        """
        return [x for x in self._list("/loadbalancers.json", "loadBalancers") \
                 if x._info['status'] == "DELETED"]

    def create(self, name, port,
               protocol, nodes, virtualIps,
               ipgroup=None, meta=None, files=None):
        """
        Create a new loadbalancer.

        #TODO: Args
        """

        if not protocol in LB_PROTOCOLS:
            raise InvalidProtocol()

        nodeDico = [x.toDict() for x in nodes]
        vipDico = [x.toDict() for x in virtualIps]
        print nodeDico

        if len(name) > 128:
            raise InvalidLoadBalancerName("LB name is too long.")

        body = {"loadBalancer": {
            "name": name,
            "port": base.getid(port),
            "protocol": protocol,
            "nodes": nodeDico,
            "virtualIps": vipDico,
            }}

        return self._create("/loadbalancers", body, "loadBalancer")

    def delete(self, loadbalancerid):
        """
        Delete load balancer.

        :param loadbalancerid: ID of the :class:`LoadBalancer` to get.
        :rtype: :class:`LoadBalancer`
        """
        self._delete("/loadbalancers/%s" % base.getid(loadbalancerid))

    def add_nodes(self, loadbalancerId, nodes):
        nodeDico = [x.toDict() for x in nodes]
        self._action('nodes', "%d/nodes" % base.getid(loadbalancerId), \
                         nodeDico)

    def delete_node(self, loadBalancerId, nodeId):
        self.api.client.delete('/loadbalancers/%d/nodes/%d' % (
                base.getid(loadBalancerId),
                base.getid(nodeId),
                ))

    def update_node(self, loadBalancerId, nodeId, dico):
        self.api.client.put('/loadbalancers/%d/nodes/%d' % (
                base.getid(loadBalancerId),
                base.getid(nodeId),
                ), body={"node": dico})

    def _action(self, action, url, info=None):
        """
        Perform a loadbalancer POST "action".
        """
        self.api.client.post('/loadbalancers/%s' % url, body={action: info})
