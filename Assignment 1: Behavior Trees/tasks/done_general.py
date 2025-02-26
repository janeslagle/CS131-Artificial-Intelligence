#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import GENERAL_CLEANING

class DoneGeneral(btl.Task):
    """
    Implementation of the Task "Done General". Clears general cleaning variable by setting it to be False.
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('DoneGeneral')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task.
        self.print_message('General Cleaning is done')

        blackboard.set_in_environment(GENERAL_CLEANING, False)
        return self.report_succeeded(blackboard)