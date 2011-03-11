# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import urllib
from cloudlb import base


def get_usage(client, lbId=None, startTime=None, endTime=None):
    dico = {}
    if startTime:
        dico['startTime'] = startTime.isoformat()
    if endTime:
        dico['endTime'] = endTime.isoformat()

    query_string = ""
    if dico:
        query_string = "?" + urllib.urlencode(dico)

    query_lb = ""
    if lbId:
        query_lb = "/%s" % (lbId)

    ret = client.get('/loadbalancers%s/usage%s' % \
                                         (query_lb, query_string))

    ret = ret[1]

    #TODO: Convert all startTime and endTime field to datetime
    if not lbId:
        return ret

    ret = ret['loadBalancerUsageRecords']
    alist = []
    for row in ret:
        row['startTime'] = base.convert_iso_datetime(row['startTime'])
        row['endTime'] = base.convert_iso_datetime(row['endTime'])
        alist.append(row)

    return alist
