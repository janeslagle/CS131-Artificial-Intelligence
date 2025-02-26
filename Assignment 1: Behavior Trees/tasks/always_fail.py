#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import SPOT_CLEANING

class AlwaysFail(btl.Task):
    """
    Implementation of the Task "Always Fail". This will always return self.report_failed no matter what!
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('AlwaysFail')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task.
        self.print_message('Task is always failing')

        return self.report_failed(blackboard)