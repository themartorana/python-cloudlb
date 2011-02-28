# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource


class Node(SubResource):
    def __repr__(self):
        return "<Node: %s:%s>" % (self._address, self._port)

    def __init__(self, address=None,
                 port=None,
                 condition=None,
                 status=None,
                 id=None,
                 **kwargs):
        self._port = port
        self._address = address
        self._condition = condition
        self._status = status
        self._id = id

        if not all([self._port, self._address, self._condition]):
            #TODO: Proper check on conditon as well
            raise Exception("You need to specify a" + \
                                " port address and a condition")

        ret = {}
        for k in self.__dict__:
            ret[k] = self.__dict__[k]
        self._add_details(ret)
