# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource


class Node(SubResource):
    def __repr__(self):
        return "<Node: %s:%s>" % (self.address, self.port)

    def __init__(self, parent=None,
                 address=None,
                 port=None,
                 condition=None,
                 status=None,
                 id=None,
                 **kwargs):
        self.port = port
        self.address = address
        self.condition = condition
        self.status = status
        self.id = id
        self._parent = parent

        if not all([self.port, self.address, self.condition]):
            #TODO: Proper check on conditon as well
            raise Exception("You need to specify a" + \
                                " port address and a condition")

    def delete(self):
        self._parent.manager.delete_node(self._parent.id,
                                         self.id, self.toDict())
