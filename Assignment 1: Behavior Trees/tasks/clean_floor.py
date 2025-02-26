#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from random import random

class CleanFloor(btl.Task):
    """
    Implementation of the Task "Cleaning Floor". 
    This task executes until failure: until there is nothing more to clean.
    Determine if there is nothing more to clean randomly with low prob. (5%) that it fails.
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('CleanFloor')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task.
        self.print_message('Cleaning the floor')

        # Determine randomly with 5% that it fails, otherwise it cleans everything and succeeds.
        if random() < 0.05:
            self.print_message('Oh no - failed to clean the entire floor!')
            return self.report_failed(blackboard)
        
        # Otherwise: cleaned everything!
        self.print_message('Successfully cleaned the entire floor - whoot whoot!')
        return self.report_succeeded(blackboard)