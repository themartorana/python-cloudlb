# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource, SubResourceDict


class NodeDict(SubResourceDict):
    def get(self, nodeId):
        for d in self.dico:
            if d.id == nodeId:
                return d

    def filter(self,
               id=None,
               condition=None,
               address=None,
               port=None,
               status=None):
        ret = []
        for d in self.dico:
            if condition and d.condition.lower() == condition.lower():
                ret.append(d)
            if address and d.address.lower() == address.lower():
                ret.append(d)
            if id and int(id) == int(id):
                ret.append(d)
            if port and int(d.port) == int(port):
                ret.append(d)
            if status and d.status.lower() == status.lower():
                ret.append(d)
        return ret


class Node(SubResource):
    def __repr__(self):
        return "<Node: %s:%s:%s>" % (self.id, self.address, self.port)

    def __init__(self,
                 weight=None,
                 parent=None,
                 address=None,
                 port=None,
                 condition=None,
                 status=None,
                 id=None,
                 **kwargs):
        self.port = port
        self.weight = weight
        self.address = address
        self.condition = condition
        self.status = status
        self.id = id
        self._parent = parent
        self._originalInfo = self.toDict(includeNone=True)

        if not all([self.port, self.address, self.condition]):
            #TODO: Proper Exceptions
            raise Exception("You need to specify a" + \
                                " port address and a condition")

    def delete(self):
        self._parent.manager.delete_node(self._parent.id,
                                         self.id,
                                         )

    def update(self):
        ret = {}
        dico = self.toDict()
        #Not allowed to update.
        dico.pop('address')
        dico.pop('port')
        for k in dico.keys():
            if k in self._originalInfo and dico[k] != self._originalInfo[k]:
                ret[k] = dico[k]
        if not ret:
            #TODO: Proper exceptions
            raise Exception("Nothing to update nothing has changed.")

        self._parent.manager.update_node(self._parent.id,
                                         self.id, ret)
