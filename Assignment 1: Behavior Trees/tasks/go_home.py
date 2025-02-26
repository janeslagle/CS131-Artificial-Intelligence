#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import HOME_PATH

class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home". It recalls the home path to return to.
    """
    def __init__(self):
        """
        Default constructor.
        """
        super().__init__('GoHome')

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task.
        self.print_message('Going home')

        # From tree diagram: go home task has blackboard operation of recalling home path so pull the home path from the blackboard
        # using HOME_PATH variable that should have already been set in find home task by the point this task is called.
        home_path = blackboard.get_in_environment(HOME_PATH, "")

        # Have 2 cases here: valid or invalid home path.
        # Invalid home path returned case.
        if not home_path:
            self.print_message('No home path found to return to')
            return self.report_failed(blackboard)

        # Valid home path returned case.
        self.print_message('Going home to path: ' + home_path)
        return self.report_succeeded(blackboard)