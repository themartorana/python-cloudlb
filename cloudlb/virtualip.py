# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import cloudlb.base


class VirtualIP(cloudlb.base.SubResource):
    def __repr__(self):
        return "<VirtualIP: %s:%s>" % (self._address, self._type)

    def __init__(self, address=None,
                 ipVersion=None,
                 type=None,
                 id=None,
                 **kwargs):
        self._address = address
        self._ipVersion = ipVersion
        self._type = type
        self._id = id
        if self._id:
            self._id = int(id)

        #TODO: check for type to be proper

        if not any([self._type, self._id]):
            #TODO: Proper check on conditon as well
            raise Exception("You need to specify a" + \
                                " type or an id (for shared ip)")
