# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"


class ConnectionLogging(object):
    type = "connectionLogging"
    path = None

    def __init__(self, client, lbId=None):
        self.lbId = lbId
        if self.lbId:
            self.lbId = int(self.lbId)
            self.path = "/loadbalancers/%s/%s" % (self.lbId, self.type.lower())

        self.client = client

    def enable(self):
        dico = {'enabled': True}
        ret = self.client.put(self.path, body={self.type: dico})
        return ret

    def disable(self):
        dico = {'enabled': False}
        ret = self.client.put(self.path, body={self.type: dico})
        return ret

    def get(self):
        ret = self.client.get("%s.json" % self.path)
        return ret[1][self.type]['enabled']
