# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.client import CLBClient
from cloudlb.loadbalancers import LoadBalancerManager
from cloudlb.node import Node
from cloudlb.virtualip import VirtualIP


class CloudLoadBalancer(object):
    """
    Top-level object to access the Rackspace Cloud Load Balancer API.

    TODO:
    """

    def __init__(self, username, api_key, region, **kwargs):
        self.client = CLBClient(username,
                                api_key,
                                region,
                                **kwargs)
        self.loadbalancers = LoadBalancerManager(self)

    def show_limits(self):
        return self.client.get("/loadbalancers/limits")[1]['limits']

    def authenticate(self):
        """
        Authenticate against the server.

        Normally this is called automatically when you first
        access the API, but you can call this method to force
        authentication right now.

        Returns on success; raises :exc:`TODO:` if the credentials
        are wrong.
        """
        self.client.authenticate()
