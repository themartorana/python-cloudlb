# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"


class ResponseError(Exception):
    """
    Raised when the remote service returns an error.
    """
    def __init__(self, status, reason):
        self.status = status
        self.reason = reason
        Exception.__init__(self)

    def __str__(self):
        return '%d: %s' % (self.status, self.reason)

    def __repr__(self):
        return '%d: %s' % (self.status, self.reason)


class InvalidRegion(Exception):
    """
    Raised when the region specified is invalid
    """
    pass


class InvalidProtocol(Exception):
    """
    Raised when the protocol specified is invalid
    """
    pass


class AuthenticationFailed(Exception):
    """
    Raised on a failure to authenticate.
    """
    pass
