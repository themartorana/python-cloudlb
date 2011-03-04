# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.client import CLBClient
from cloudlb.loadbalancers import LoadBalancerManager
from cloudlb.node import Node
from cloudlb.virtualip import VirtualIP
from cloudlb.consts import VERSION
from usage import get_usage
from cloudlb import base

__version__ = VERSION

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

    def usage(self, startTime=None, endTime=None):
        startTime = startTime and startTime.isoformat()
        endTime = endTime and endTime.isoformat()
        ret = get_usage(self.client, startTime=startTime, endTime=endTime)
        return ret

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
