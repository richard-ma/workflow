from unittest import TestCase

from workflow import *

class ActionTestCase(TestCase):
    def setUp(self):
        self.action = Action()

    def tearDown(self):
        pass

    def test_action_run(self):
        self.assertEqual(None, self.action.run())
