#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl

class Priority(btl.Composite):
    """
    Impelmentation of priority composite. 
    Children evaluated in order of priority: ignore any running child.
    
    Returns:
        - succ as soon as one of children returns succ
        - failed if all children have returned failed
        - running immed. if child returns running
    """

    def __init__(self, name: str, children: btl.NodeListType):
        """
        Need the children here.
        """
        super().__init__(name, children)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        Loop through all children have one by one:
            - if current child looping over succ return succ
            - if current child looping over running return running
            - else: only go to next child in loop if child failed so will know to return failure if have exited for loop and haven't returned anything yet

        """
        for child in self.children:
            result_child = child.run(blackboard)

            if result_child == btl.ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard)
            elif result_child == btl.ResultEnum.RUNNING:
                return self.report_succeeded(blackboard)
            
        return self.report_failed(blackboard)