# -*- encoding: utf-8 -*-
""" Base object class, basically the same class taken
from jacobian python-cloudservers library"""
import datetime


class Resource(object):
    """ A resource represents a particular instance of an object
    (loadbalancers, protocol, etc). This is pretty much just a bag for
    attributes.  """
    def __init__(self, manager, info):
        self.manager = manager
        self._info = info
        self._add_details(info)

    def _add_details(self, info):
        for (k, v) in info.iteritems():
            setattr(self, k, v)

    def __getattr__(self, k):
        self.get()
        if k not in self.__dict__:
            raise AttributeError("Object has no attribute '%s'" % k)
        else:
            return self.__dict__[k]

    def __repr__(self):
        reprkeys = sorted(k for k in self.__dict__.keys() \
                              if k[0] != '_' and k != 'manager')
        info = ", ".join("%s=%s" % (k, getattr(self, k)) for k in reprkeys)
        return "<%s %s>" % (self.__class__.__name__, info)

    def get(self):
        new = self.manager.get(self.id)
        self._add_details(new._info)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if hasattr(self, 'id') and hasattr(other, 'id'):
            return self.id == other.id
        return self._info == other._info


class Manager(object):
    """ Managers interact with a particular type of API (loadbalancer,
    protocol, etc.) and provide CRUD operations for them."""
    resource_class = None

    def __init__(self, api):
        self.api = api

    def _list(self, url, response_key):
        resp, body = self.api.client.get(url)
        return [self.resource_class(self, res) for res in body[response_key]]

    def _get(self, url, response_key):
        resp, body = self.api.client.get(url)
        return self.resource_class(self, body[response_key])

    def _create(self, url, body, response_key):
        resp, body = self.api.client.post(url, body=body)
        return self.resource_class(self, body[response_key])

    def _delete(self, url):
        resp, body = self.api.client.delete(url)

    def _update(self, url, body):
        resp, body = self.api.client.put(url, body=body)


class ManagerWithFind(Manager):
    """
    Like a `Manager`, but with additional `find()`/`findall()` methods.
    """
    def find(self, **kwargs):
        """
        Find a single item with attributes matching ``**kwargs``.

        This isn't very efficient: it loads the entire list then filters on
        the Python side.
        """
        rl = self.findall(**kwargs)
        try:
            return rl[0]
        except IndexError:
            #TODO:
            # NotFound(404, "No %s matching %s." %
            # (self.resource_class.__name__, kwargs))
            raise Exception()

    def findall(self, **kwargs):
        """
        Find all items with attributes matching ``**kwargs``.

        This isn't very efficient: it loads the entire list then filters on
        the Python side.
        """
        found = []
        searches = kwargs.items()

        for obj in self.list():
            try:
                if all(getattr(obj, attr) == value \
                           for (attr, value) in searches):
                    found.append(obj)
            except AttributeError:
                continue

        return found


class SubResource(object):
    """
    Resources attached to a main resource but not accessed
    directly from the API. Like the repr of a dict inside a dict.
    """
    def __getattr__(self, k):
        if '_%s' % (k) in self.__dict__:
            return self.__dict__['_%s' % (k)]
        else:
            raise AttributeError(k)

    def toDict(self):
        """
        Convert the local attributes to a dict
        """
        ret = {}
        for attr in self.__dict__:
            if self.__dict__[attr]:
                ret[attr.replace("_", "")] = self.__dict__[attr]
        return ret

    def _add_details(self, info):
        for (k, v) in info.iteritems():
            if k.startswith("_") and self.__dict__[k]:
                setattr(self, k.replace("_", ""), v)


def getid(obj):
    """
    Abstracts the common pattern of allowing both an object or an object's ID
    (integer) as a parameter when dealing with relationships.
    """
    try:
        return obj.id
    except AttributeError:
        return int(obj)


def convert_time(dt):
    """
    Convert iso8601 to datetime
    """
    isoFormat = "%Y-%m-%dT%H:%M:%S+0000"
    if type(dt) is datetime.datetime:
        return dt
    return datetime.datetime.strptime(dt, isoFormat)
