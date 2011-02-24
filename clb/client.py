# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"
import httplib2
import os

import consts


class CLBClient(httplib2.Http):
    """
    Client class for accessing the CLB API.
    """

    def __init__(self,
                 username,
                 api_key,
                 region,
                 auth_url=consts.DEFAULT_AUTH_SERVER):
        super(CLBClient, self).__init__()
        self.username = username
        self.api_key = api_key
        self.region = region
        self._auth_url = auth_url

        if region.lower() in consts.REGION.keys():
            pass

        self.auth_token = None
        self.account_number = None

    def authenticate(self):
        headers = {'X-Auth-User': self.username, 'X-Auth-Key': self.api_key}
        resp, body = self.request(self._auth_url, 'GET', headers=headers)
        self.account_number = os.path.basename(resp['x-server-management-url'])
        self.auth_token = resp['x-auth-token']

if __name__ == '__main__':
    c = CLBClient("chmouelb", "1043efb7cd05474fb10dc60671c1d78d", "ord")
    c.authenticate()
    print c.account_number
