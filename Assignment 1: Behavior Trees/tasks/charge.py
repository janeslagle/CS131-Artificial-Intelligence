#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import BATTERY_LEVEL, CHARGING

class Charge(btl.Task):
    """
    Implementation of the Task "Charge". It implements blackboard operation of charging the battery level.
    Assumes that it fully charges the battery to 100% upon call of this task.
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('Charge')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task.
        self.print_message('Charging battery to 100%')

        blackboard.set_in_environment(BATTERY_LEVEL, 100)
        return self.report_succeeded(blackboard)