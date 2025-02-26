#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl

class DoNothing(btl.Task):
    """
    Implementation of the Task "Do Nothing". Literally, do nothing except print out task doing and return succeeded state.
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('DoNothing')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task.
        self.print_message('Doing nothing')
        
        return self.report_succeeded(blackboard)