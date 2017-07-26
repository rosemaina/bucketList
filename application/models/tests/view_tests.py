"""This is the main module for testing flask"""
from flask import Flask
from flask_testing import TestCase
from application.views import *

class TestBucketApp(TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_register(self):

        response = self.client.get('/registration', data)
        user = 
        self.assertEqual(response.status_code, 200)
        print (response)
