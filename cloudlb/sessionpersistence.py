# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
from cloudlb.base import SubResource, SubResourceManager
from cloudlb.consts import SESSION_PERSISTENCE_TYPES


class SessionPersistence(SubResource):
    def __repr__(self):
        return "<SessionPersistence: %s>" % (self.persistenceType)

    def __init__(self, persistenceType=None):
        self.persistenceType = persistenceType

        if not self.persistenceType:
            raise Exception("You need to specify a persistenceType.")

        if not self.persistenceType in SESSION_PERSISTENCE_TYPES:
            raise Exception("%s is an invalid session persistence type" % (
                    self.type))


class SessionPersistenceManager(SubResourceManager):
    path = None
    type = "sessionPersistence"
    resource = SessionPersistence
