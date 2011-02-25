# -*- encoding: utf-8 -*-
__author__ = "Chmouel Boudjnah <chmouel@chmouel.com>"

import unittest
import os
import cloudlb.client
import cloudlb.errors


class TestClient(unittest.TestCase):
    def setUp(self):
        self.username = os.environ.get("RCLOUD_USER", None)
        self.api_key = os.environ.get("RCLOUD_KEY", None)
        self.region = "ord"

        if not all([self.username, self.api_key]):
            print """
You have not defined your environement variable properly for the unit tests.
Please adjust your RCLOUD_USER, RCLOUD_KEY variables to be able
to launch the tests.
"""
            self.assertTrue(False)

    def test_constructor(self):
        """
        Test passing argument to constructor.
        """

        region = "ord"
        client = cloudlb.client.CLBClient(self.username,
                                      self.api_key,
                                      region)
        self.assertTrue(client.region == "ord")

        region = "chicago"
        client = cloudlb.client.CLBClient(self.username,
                                      self.api_key,
                                      region)
        self.assertTrue(client.region == "ord")

        callit = lambda: cloudlb.client.CLBClient(self.username,
                                              self.api_key,
                                              "nowhere")
        self.assertRaises(cloudlb.errors.InvalidRegion,
                          callit)

    def test_auth(self):
        client = cloudlb.client.CLBClient(self.username,
                                      self.api_key,
                                      self.region)
        client.authenticate()
        self.assert_(client.auth_token)
        self.assert_(type(client.account_number) is int)

        client = cloudlb.client.CLBClient("memyself",
                                      "andI....",
                                      self.region)
        self.assertRaises(cloudlb.errors.AuthenticationFailed,
                          client.authenticate)

        client = cloudlb.client.CLBClient("memyself",
                                      "andI....",
                                      self.region,
                                      auth_url="http://www.google.com")
        self.assertRaises(cloudlb.errors.ResponseError,
                          client.authenticate)

    def test_get(self):
        client = cloudlb.client.CLBClient(self.username,
                                      self.api_key,
                                      self.region)
        r, b = client.get("/loadbalancers")
        self.assertEqual(r.status, 200)

        callme = lambda: client.get("/loadbalancersf")
        self.assertRaises(cloudlb.errors.ResponseError, callme)
