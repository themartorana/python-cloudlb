# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource, SubResourceManager
from cloudlb.consts import SESSION_PERSISTENSE_TYPES


class SessionPersistense(SubResource):
    def __repr__(self):
        return "<SessionPersistense: %s>" % (self.persistenceType)

    def __init__(self, persistenceType=None):
        self.persistenceType = persistenceType

        if not self.persistenceType:
            raise Exception("You need to specify a persistenceType.")

        if not self.persistenceType in SESSION_PERSISTENSE_TYPES:
            raise Exception("%s is an invalid session persistence type" % (
                    self.type))


class SessionPersistenseManager(SubResourceManager):
    path = None
    type = "sessionPersistence"
    resource = SessionPersistense
