#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import SPOT_CLEANING

class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    Implements clearning SPOT_CLEANING variable by setting it to be False.
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('DoneSpot')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task.
        self.print_message('Setting spot cleaning to done')

        # Updates SPOT_CLEANING to T when command requested.
        blackboard.set_in_environment(SPOT_CLEANING, False)
        return self.report_succeeded(blackboard)