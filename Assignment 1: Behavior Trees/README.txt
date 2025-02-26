# Tufts CS 131 - Artificial Intelligence
# Assignment 01 - Behavior Trees
# Jane Slagle

To Run:
- Run main.py
    Everything for simulating the behavior of the vacuum is contained within the function main() in main.py
- Make sure the random library is installed

Assumptions:
In main() in main.py:
    General Assumptions:
        (1) vaccum starts with an initial battery level of 29%
        (2) user selects one of the following tasks at the start of the simulation:
            - spot cleaning 
            - general cleaning  
            - shut off (which ends the simulation)
        (3) there is a 15% chance that a dusty spot is detected, which is determined randomly
        (4) once a task is completely finished and the robot has no more tasks left, the user is prompted to chose the next task for the vacuum

    Termination Conditions:
        (1) if the vaccum runs out of battery (battery level 0%) and is not recharged during the simulation
        (2) if the vacuum is done with all of its tasks and is doing nothing and the user chooses to power it off instead of assigning it another task

In tasks:
    Clean Floor Task:
        (1) it is randomly determined with a 5% chance that the vaccum will fail to clean the entire floor

    Charge Task:
        (1) Assumes that the vaccum's battery is charged to 100% when this task is called


Results:
    Displays the progress of the task specified by the user, providing a walkthrough of the decision tree as the vacuum exectues the task.
    Shows whether the task is running, successful or failed until it completes.
