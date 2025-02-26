#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import SPOT_CLEANING

class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "spot cleaning". 
    """

    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('SpotCleaning')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking if spot cleaning is occuring')

        if blackboard.get_in_environment(SPOT_CLEANING, False):
            # Means have set variable to True + only set it to True when spot cleaning has actually happened.
            return self.report_succeeded(blackboard)
        else:
            # Means condition not met --> failed.
            return self.report_failed(blackboard)