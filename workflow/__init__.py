__all__ = ['Action', 'Workflow']

import queue


class Action(object):
    def __init__(self, **kwargs):
        self.params = kwargs

    def run(self, *data):
        return None


class Workflow(object):
    def __init__(self):
        self.actions = queue.Queue()

    def push(self, action: Action):
        self.actions.put(action)
        return self

    def execute(self):
        data = None
        while self.actions.qsize() > 0:
            action = self.actions.get()
            data = action.run(data)
            # Break processing of workflow when previous action data is False
            if data == False:
                return False
        return True


# Usage
#
#if __name__ == "__main__":
#Workflow(
#).push(Action(hello='world')
#).push(Action(buy='buy buy')
#).execute()
