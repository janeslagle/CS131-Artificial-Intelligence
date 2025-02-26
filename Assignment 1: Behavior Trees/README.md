## Tufts CS 131 - Artificial Intelligence
## Assignment 01 - Behavior Trees
## Jane Slagle  


### To Run:
- Run `main.py` 
  - Everything for simulating the behavior of the vacuum is contained within the function `main()` in `main.py`
- Ensure the `random` library is installed


### Assumptions:

**General Assumptions (In `main.py` → `main()`):**
1. The vacuum starts with an initial battery level of 29%
2. The user selects one of the following tasks at the start of the simulation:  
   - Spot Cleaning
   - General Cleaning  
   - Shut Off (which ends the simulation).  
3. There is a 15% chance that a dusty spot is detected (randomly determined)  
4. Once a task is completed and the robot has no more tasks left, the user is prompted to choose the next task  

**Termination Conditions:**
1. The vacuum runs out of battery (battery level 0%) and is not recharged during the simulation
2. The vacuum finishes all tasks and the user chooses to power it off instead of assigning another task

**Task Details:**
**Clean Floor Task**
- There is a 5% chance that the vacuum will fail to clean the entire floor (randomly determined) 

**Charge Task**
- Assumes that the vacuum's battery is charged to 100% when this task is called 


### Results:
- Displays the progress of the selected task in real time
- Provides a walkthrough of the decision tree as the vacuum executes the task
- Shows whether the task is:  
  - Running  
  - Successful  
  - Failed  
- The simulation continues until the task is completed
