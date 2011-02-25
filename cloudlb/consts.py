# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
VERSION = 0.1
USER_AGENT = 'python-cloudb/%s' % VERSION

DEFAULT_AUTH_SERVER = "https://auth.api.rackspacecloud.com/v1.0"

REGION = {
    "chicago": "ord",
    "dallas": "dfw",
}

REGION_URL = "https://%s.loadbalancers.api.rackspacecloud.com/v1.0"

LB_PROTOCOLS = ["FTP", "HTTP", "IMAPv4", "POP3", "LDAP",
              "LDAPS", "HTTPS", "IMAPS",
              "POP3S", "SMTP"]
