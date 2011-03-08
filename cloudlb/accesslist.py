# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource


class NetworkItem(SubResource):
    def __repr__(self):
        return "<NetworkItem: %s:%s>" % (self.address, self.type)

    def __init__(self, parent=None,
                 address=None,
                 type=None,
                 id=None):
        self.address = address
        self.type = type
        self.id = id
        self._parent = parent
        self._originalInfo = self.toDict(includeNone=True)

        if not all([self.address, self.type]):
            #TODO: Proper Exceptions
            raise Exception("You need to specify an" + \
                                " address and a type.")


class AccessList(object):
    def __init__(self, client, lbId=None):
        self.lbId = lbId
        if self.lbId:
            self.lbId = int(self.lbId)
            self.path = "/loadbalancers/%s/accesslist" % self.lbId

        self.client = client

    def get(self, id):
        objects = self.list()
        for obj in objects:
            if obj.id == id:
                return obj
        #TODO: Not found Exceptions or None ?

    def list(self):
        ret = self.client.get("%s.json" % self.path)
        return [NetworkItem(**x) for x in ret[1]['accessList']]

    def add(self, networkitems):
        dico = [x.toDict() for x in networkitems]
        self.client.post(self.path, body=dico)

    def delete(self, id=None):
        extrapath = ""
        if id:
            extrapath = "/%d" % (id)
        self.client.delete("%s%s" % (self.path, extrapath))
