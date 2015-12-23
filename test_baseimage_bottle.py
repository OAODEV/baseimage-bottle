import os
import unittest
import uuid

from config_finder import cfg
import bottle

class BaseimageBottleTests(unittest.TestCase):

    def setUp(self):
        self.config_key = str(uuid.uuid4())
        self.config_val = str(uuid.uuid4())
        os.environ[self.config_key] = self.config_val

    def tearDown(self):
        del os.environ[self.config_key]

    def test_config_finder_operational(self):
        """ this container should have access to config_finder """
        self.assertEqual(self.config_val, cfg(self.config_key))

    def test_bottle_operational(self):
        """ this container should have access to bottle """
        app = bottle.default_app()
        self.assertTrue(isinstance(app, bottle.Bottle))

    def test_psycopg2_installed(self):
        import psycopg2
