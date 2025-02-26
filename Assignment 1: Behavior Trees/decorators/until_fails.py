#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.decorator import Decorator
from bt_library.tree_node import TreeNode

class UntilFails(Decorator):
    """
    Implementation of "until fails" decorator: 
        - returns running when child returns succeeded or running
        - returns succeeded when child rturns failed

    Associated with the "clean floor" task, so indicates if stopping cleaning floor or keep going.
    """

    def __init__(name: str, child: TreeNode):
        """
        Get the child associated to the decorator out.
        """
        super().__init__("Until Fails", child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node by figuring out what the child is doing.
        """

        # Evaluate the child
        result_child = self.child.run(blackboard)

        if result_child == ResultEnum.RUNNING:
            # Means keep cleaning floor so indicate so to user.
            self.print_message('Still cleaning the floor')
            return self.report_running(blackboard)
        elif result_child == ResultEnum.SUCCEEDED:
            # Means keep cleaning floor so indicate so to user.
            self.print_message('Still cleaning the floor')
            return self.report_running(blackboard)
        elif result_child == ResultEnum.FAILED:
            # Means have finished.
            self.print_message('Done cleaning the floor')
            return self.report_succeeded(blackboard)