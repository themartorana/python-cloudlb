# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource, SubResourceManager


class ConnectionThrottle(SubResource):
    def __repr__(self):
        return "<ConnectionThrottle>" % (self.type)

    def __init__(self,
                 minConnections=None,
                 maxConnections=None,
                 rateInterval=None,
                 maxConnectionRate=None,
                 ):
        self.minConnections = minConnections
        self.maxConnections = maxConnections
        self.rateInterval = rateInterval
        self.maxConnectionsRate = maxConnectionRate

        if not all([minConnections, maxConnections,
                    rateInterval, maxConnectionRate]):
            #TODO:
            raise Exception("missing some parameters")


class ConnectionThrottleManager(SubResourceManager):
    type = "connectionThrottle"
    resource = ConnectionThrottle
