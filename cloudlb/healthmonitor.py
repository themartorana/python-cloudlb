# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource
from cloudlb.consts import HEALTH_MONITOR_TYPES


class HealthMonitorManager(object):
    path = None
    type = "healthMonitor"

    def __init__(self, client, lbId=None):
        self.lbId = lbId
        if self.lbId:
            self.lbId = int(self.lbId)
            self.path = "/loadbalancers/%s/%s" % (self.lbId, self.type.lower())

        self.client = client

    def get(self):
        ret = self.client.get("%s.json" % self.path)
        return ret[1][self.type]

    def add(self, hm):
        dico = hm.toDict()
        ret = self.client.put(self.path, body=dico)
        return ret

    def delete(self):
        ret = self.client.delete(self.path)
        return ret

class HealthMonitor(SubResource):
    def __repr__(self):
        return "<HealthMonitor: %s:%s>" % (self.type)

    def __init__(self, type=None,
                 delay=None,
                 timeout=None,
                 attemptsBeforeDeactivation=None,
                 path=None,
                 statusRegex=None,
                 bodyRegex=None):
        self._originalInfo = self.toDict(includeNone=True)

        self.type = type
        self.delay = delay
        self.timeout = timeout
        self.attemptsBeforeDeactivation = attemptsBeforeDeactivation

        if not all([self.type, self.delay,
                    self.timeout, self.attemptsBeforeDeactivation]):
            #TODO: Proper Exceptions
            raise Exception("You need to specify a" + \
                                " type timeout and attte.")

        if not self.type in HEALTH_MONITOR_TYPES:
            raise Exception("%s is an invalid healthmonitor type" % (
                    self.type))

        if self.type in ("HTTP", "HTTPS"):
            self.path = path
            self.statusRegex = statusRegex
            self.bodyRegex = bodyRegex

            #TODO: Documentation says that statusRegex or bodyRegex
            #can be "" but that come back NULL
            if not all([path, statusRegex, bodyRegex]):
                raise Exception("You need to specify a path statusregexp " +
                                "and bodyregexp with HTTP(S) monitor")
