# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import cloudlb.base


class VirtualIP(cloudlb.base.SubResource):
    def __repr__(self):
        return "<VirtualIP: %s:%s>" % (self.address, self.type)

    def __init__(self, address=None,
                 ipVersion=None,
                 type=None,
                 id=None,
                 parent=None,
                 **kwargs):
        self.address = address
        self.ipVersion = ipVersion
        self.type = type
        self.id = id
        if self.id:
            self.id = int(id)
        self._parent = parent

        #TODO: check for type to be a proper one passed

        if not any([self.type, self.id]):
            #TODO: Proper check on conditon as well
            raise Exception("You need to specify a" + \
                                " type or an id (for shared ip)")
