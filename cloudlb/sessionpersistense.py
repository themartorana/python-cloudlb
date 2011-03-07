# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource
from cloudlb.consts import SESSION_PERSISTENSE_TYPES


class SessionPersistenseManager(object):
    path = None
    type = "sessionPersistence"

    def __init__(self, client, lbId=None):
        self.lbId = lbId
        if self.lbId:
            self.lbId = int(self.lbId)
            self.path = "/loadbalancers/%s/%s" % (self.lbId, self.type.lower())

        self.client = client

    def get(self):
        ret = self.client.get("%s.json" % self.path)
        return ret[1][self.type]

    def add(self, ssp):
        dico = ssp.toDict()
        ret = self.client.put(self.path, body={self.type: dico})
        return ret

    def delete(self):
        ret = self.client.delete(self.path)
        return ret


class SessionPersistense(SubResource):
    def __repr__(self):
        return "<SessionPersistense: %s>" % (self.type)

    def __init__(self, persistenceType=None):
        self.persistenceType = persistenceType

        if not self.persistenceType:
            raise Exception("You need to specify a persistenceType.")

        if not self.persistenceType in SESSION_PERSISTENSE_TYPES:
            raise Exception("%s is an invalid session persistense type" % (
                    self.type))
