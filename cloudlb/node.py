# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import cloudlb.base


class Node(cloudlb.base.SubResource):
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
