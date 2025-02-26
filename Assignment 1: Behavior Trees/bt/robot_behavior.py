#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt as bt
import bt_library as btl

# Instantiate the tree according to the assignment. 

# tree_root splits off into 3 different branches, so implement those 3 branches and then put them all together at the end

# 1st Branch deals with everything battery related.
# From diagram: checks battery level, then calls find home task, then go home task, then charge task.
checking_battery_seq = bt.composites.Sequence(
    "Checking Battery Sequence",
    [
        bt.conditions.BatteryLessThan30(),
        bt.tasks.FindHome(),
        bt.tasks.GoHome(),
        bt.tasks.Charge()
    ]
)

# Now implement all parts inside brnach 2 from root node.
# Start with very L sequence = spot cleaning for 20 seconds with Timer decorator = based on spot cleaning condition.
spot_cleaning_seq = bt.Sequence(
    "20 Second Spot Cleaning Sequence",
    [
        bt.conditions.SpotCleaning(),
        bt.decorators.Timer("Timer", 20, bt.tasks.CleanSpot(total_time=20)),
        bt.tasks.DoneSpot()
    ]
)

# Now do general cleaning condition sequence from branch 2.
# Starts with call to general cleaning task, then have another sequence inside that has 2 offshoots: a priority node + done general task call.
# Do left side 1st: the priority node then do done general task call.
# Then do left side inside priority before the right.
general_cleaning_seq = bt.Sequence(
    "General Cleaning Sequence",
    [
        bt.conditions.GeneralCleaning(),
        bt.composites.Priority(
            "General Cleaning Priority",
            [
            bt.composites.Sequence(
                "General Cleaning Priorty Sequence",
            [
                bt.conditions.SpotCleaning(),
                bt.decorators.Timer("Timer", 35, bt.tasks.CleanSpot(total_time=35)),
                bt.tasks.AlwaysFail()
            ]),
            bt.decorators.UntilFails(bt.tasks.CleanFloor())
        ]),
        bt.tasks.DoneGeneral()
    ]
)

# Start with very top of tree at its root node: have an initial priority node that splits off into 3 branches.
# Have to call checking_battery_seq, then inside a selection composite call spot cleaning seq + gen cleaning seq + then outside that call do nothing task.
tree_root = bt.Priority(
    "Root Priority",
    [
        checking_battery_seq,
        bt.composites.Selection(
            "Root Selection",
            [
            spot_cleaning_seq,
            general_cleaning_seq
        ]),
        bt.tasks.DoNothing()
    ]
) 

# Store the root node in a behavior tree instance.
robot_behavior = btl.BehaviorTree(tree_root)