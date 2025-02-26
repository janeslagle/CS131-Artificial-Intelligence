#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#

import bt_library as btl
from ..globals import SPOT_CLEANING

class CleanSpot(btl.Task):
    """
    Implementation of the Task "Clean Spot".
    Performs 20s intensive cleaning in specific area.
    Updates SPOT_CLEANING variable by setting it to be T if command requested, F otherwise.
    Only update once command fully completed so F case is done task's problem, not this ones.
    This can also be used to perform 35s spot cleaning since have put total_time in as param when create an instance of this task!
    So can use for clean spot with both 20s and 35s!
    """

    def __init__(self, total_time):
        """
            Default constructor. Initializes variable that use to keep track for if amount of time on timer (20 seconds) has run out for task or not. 
            Will start at 20 and then count down from there while the task is executing to make sure that the entire 20 second timer plays out.
            Define an init to do this because otherwise if set it in run(), it will reset the counter when it shouldn't be, so this avoids that.
        """
        super().__init__('CleanSpot')
        self.total_time = total_time

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        # Print statement with name of task
        self.print_message('Cleaning Spot')

        # Decrement timer, letting the user know how much time is left the entire time
        if self.total_time > 0:
            self.print_message(str(self.total_time) + " seconds left to spot clean")
            self.total_time -= 1
            return self.report_running(blackboard)
        
        # Once 20 seconds are done indicate success + update spot cleaning to now be true since 20 second task fully completed
        # Also Updates SPOT_CLEANING to be T since now 20 second task fully completed (will reset to be F in done spot task as indicated by tree diagram!)
        self.print_message("Spot cleaning is now fully complete!")

        # only want to set if not 35s spot cleaning (only want set T if doing a 20s cleaning)
        blackboard.set_in_environment(SPOT_CLEANING, True)

        return self.report_succeeded(blackboard)