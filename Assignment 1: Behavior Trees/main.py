#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 4.0.0 - copyright (c) 2023-2024 Santini Fabrizio. All rights reserved.
#

import bt_library as btl

from bt.robot_behavior import robot_behavior
from bt.globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH, CHARGING
from random import random

def main():
    # Main body of the assignment, where simulate the robot cleaning.

    # Initialize the blackboard.
    current_blackboard = btl.Blackboard()

    # Now initialize the variables to store in the blackboard, these are its default starting values.
    current_blackboard.set_in_environment(BATTERY_LEVEL, 29)
    current_blackboard.set_in_environment(SPOT_CLEANING, False)
    current_blackboard.set_in_environment(GENERAL_CLEANING, True)
    current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)
    current_blackboard.set_in_environment(HOME_PATH, "")
    current_blackboard.set_in_environment(CHARGING, False)

    # Ask user how they want to start simulation of vacuum out - simulate user input commands.
    while True:
        # Keep prompting user for a valid input until they give one of the available choices.
        user_choice = input("\nWhat task should the vacuum complete? \n Please enter 'spot' for spot cleaning, 'general' for general cleaning, or 'shut off' to power the vacuum off:\n")
        if user_choice == 'spot':
            # Move on to simulation loop below with spot cleaning set to be True.
            current_blackboard.set_in_environment(SPOT_CLEANING, True)
            break   
        elif user_choice == 'general':
            # Move on to simulation loop below with general cleaning set to be True.
            current_blackboard.set_in_environment(GENERAL_CLEANING, True)
            break 
        elif user_choice == 'shut off':
            # Exit and be done.
            print("\n Powering vacuum off. Goodbye!")
            return  
        else:
            # Means user did not input one of the vaild options, so prompt them again.
            print("\nThe command you entered was invalid. Please try again.\n")

    cycle_num = 1
    done = False
    while not done:
        print("")
        print('--------------------------------------------------------------------------------------------------------------------')
        print("Starting cycle: " + str(cycle_num) +"\n")
        # Each cycle in this while-loop is equivalent to 1 second time.

        # Step 1: Change the environment - change battery level.
        # Each cycle: takes up 1% of vacuum's battery.
        curr_battery_level = current_blackboard.get_in_environment(BATTERY_LEVEL, 0)
        updated_battery_level = curr_battery_level - 1
        current_blackboard.set_in_environment(BATTERY_LEVEL, updated_battery_level)

        # Termination case: if the vacuum dies and it is not recharged.
        if updated_battery_level == 0:
            print("Vacuum died, powering off.")
            done = True
            return

        # Simulate the response of the dusty spot sensor.
        # Simulate dusty spot sensor vaule generator as random generator - dusty spot detected with 15% chance.
        if random() < 0.15:
            # Let user know that dusty spot was detected so that it knows what the vacuum is doing.
            current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, True)
            print("Sensor detected a dusty spot during the cycle \n")
        else:
            current_blackboard.set_in_environment(DUSTY_SPOT_SENSOR, False)

        # Step 2: Evaluating the behavior tree.
        result = robot_behavior.evaluate(current_blackboard)

        # Check if the robot is done running the given task. This means that it is not still actively running a task and will mean that the spot and
        # general cleaning variables will be set to False. If all of this is true, then means the robot finished its task and is not currently doing 
        # anything.
        # So prompt the user to see what they want the robot to do next since the robot is just sitting there now.
        if result != btl.ResultEnum.RUNNING:
            if not current_blackboard.get_in_environment(SPOT_CLEANING, True) and not current_blackboard.get_in_environment(GENERAL_CLEANING, True):
                print('--------------------------------------------------------------------------------------------------------------------')
                user_choice = input("\n All tasks completed. What task should the vacuum complete next? \n Please enter 'spot' for spot cleaning, 'general' for general cleaning, or 'shut off' to power the vacuum off:\n")

                if user_choice == 'spot':
                    # Activate spot cleaning for all cycles with this next task.
                    current_blackboard.set_in_environment(SPOT_CLEANING, True)
                elif user_choice == 'general':
                    # Activate general cleaning for all cycles with this next task.
                    current_blackboard.set_in_environment(GENERAL_CLEANING, True)
                elif user_choice == 'shut off':
                    # Stop the simulation entirely.
                    print("")
                    print("Powering vacuum off. Goodbye!")
                    done = True 
                else:
                    # Means user did not input valid option, so prompt them again for valid choice.
                    print("\nThe command you entered was invalid. Please try again.\n")

        # Update cycle for next run through for print statements.
        cycle_num += 1

if __name__ == '__main__':
    main()

    pass