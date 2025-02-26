#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import GENERAL_CLEANING

class GeneralCleaning(btl.Condition):
    """
    Implementation of the condition "dusty spot". 
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('GeneralCleaning')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Checking if general cleaning is occuring')

        if blackboard.get_in_environment(GENERAL_CLEANING, False):
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)