# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
VERSION = "0.1"
USER_AGENT = 'python-cloudb/%s' % VERSION

# Default AUTH SERVER
DEFAULT_AUTH_SERVER = "https://auth.api.rackspacecloud.com/v1.0"

# Default URL for Regions
REGION_URL = "https://%s.loadbalancers.api.rackspacecloud.com/v1.0"

# Different available Regions
REGION = {
    "chicago": "ord",
    "dallas": "dfw",
}

# Allowed Protocol
LB_PROTOCOLS = ["FTP", "HTTP", "IMAPv4", "POP3", "LDAP",
                "LDAPS", "HTTPS", "IMAPS",
                "POP3S", "SMTP"]

# Attributed allowed to be modified on loadbalancers
LB_ATTRIBUTES_MODIFIABLE = ["name", "algorithm", "protocol", "port"]

# Types of VirtualIPS
VIRTUALIP_TYPES = ["PUBLIC", "SERVICENET"]

# HealthMonitors Types
HEALTH_MONITOR_TYPES = ['CONNECT', 'HTTP', 'HTTPS']
