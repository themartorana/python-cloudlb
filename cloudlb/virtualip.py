# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import cloudlb.base


class VirtualIP(cloudlb.base.SubResource):
    def __init__(self, address=None,
                 ipVersion=None,
                 type=None,
                 id=None,
                 **kwargs):
        self._address = address
        self._ipVersion = ipVersion
        self._id = id
        self._type = type

        if not all([self._type]):
            #TODO: Proper check on conditon as well
            raise Exception("You need to specify a" + \
                                " port address and a condition")
