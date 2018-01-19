from unittest import TestCase

from workflow import *

class WorkflowTestCase(TestCase):
    def setUp(self):
        self.action = Action()
        self.workflow = Workflow()

    def tearDown(self):
        pass

    def test_workflow_push(self):
        re = self.workflow.push(self.action)
        self.assertEqual(self.workflow, re)

    def test_workflow_execute(self):
        re = self.workflow.execute()
        self.assertEqual(True, re)

        re = self.workflow.push(self.action).execute()
        self.assertEqual(True, re)
