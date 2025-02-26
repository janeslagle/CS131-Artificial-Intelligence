#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl
from ..globals import HOME_PATH

class FindHome(btl.Task):
    """
    Implementation of the Task "Find Home".
    """

    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('FindHome')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Looking for a home')

        # Left the example path given in code skeleton.
        blackboard.set_in_environment(HOME_PATH, 'Up Left Left Up Right')

        return self.report_succeeded(blackboard)