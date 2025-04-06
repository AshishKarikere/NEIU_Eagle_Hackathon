# NEIU_Eagle_Hackathon

Create a Task Manager Simulator that helps users manage their daily tasks efficiently.

Your Task Manager Simulator program must allow users to:

Add a Task: A task consists of a title (string), a priority level (1 = high, 2 = medium, 3 = low), and a time estimate in minutes (integer).
View All Tasks: Display a list of all tasks sorted by priority (high to low). If two tasks have the same priority, sort them by the time estimate (shortest first).
Complete a Task: Mark a task as complete, which should remove it from the task list.
Undo Last Action: Allow the user to undo their last action (adding, completing a task, or viewing the list).
Exit: End the program.

Time breakdown

1. Setting Up the Environment and Understanding the Problem (15 minutes)

Reading and understanding the problem statement, creating project files, and setting up the development environment.
2. Implementing the Task Data Structure (25 minutes)

Define a Task class with attributes: title, priority, timeEstimate, and a pointer to the next task.
Create a TaskNode for linked list implementation.
Key Methods: Constructor, getters, and setters.
3. Implementing the Linked List for Task Management (30 minutes)

Create methods for adding a task, displaying tasks sorted by priority and time, and removing tasks. Implement a linked list class to manage these tasks. Key Methods: addTask(), viewTasks(), removeTask(). Time: 30 minutes

4. Implementing the Stack for Undo Feature (30 minutes)

Define a Stack class to store actions for undo functionality. Implement push(), pop(), and undo() methods. Key Methods: addTaskToStack(), removeTaskFromStack(), undoLastAction(). Time: 30 minutes

5. Building the Menu System (25 minutes)

Create a loop with menu options: Add Task, View Tasks, Complete Task, Undo Last Action, Exit. Handle user input and call corresponding methods. Key Methods: showMenu(), input validation, switch-case or if-else logic. Time: 25 minutes

6. Testing and Debugging (30 minutes)

Test each feature: adding tasks, viewing sorted tasks, completing tasks, and undoing actions. Fix bugs and ensure a smooth user experience. Time: 30 minutes

7. Bonus Challenges (Optional - 25 minutes)

Implement search by task title. Save tasks to a file and load on startup. Edit tasks (title or time estimate). Time: 25 minutes (if students finish early).

8. Final Testing and Code Cleanup (15 minutes) Task: Ensure code readability, proper comments, and final testing. Handle edge cases (empty list, invalid input). Time: 15 minutes

Total Estimated Time: 3 Hours (180 minutes) This breakdown balances core functionality with testing and optional features, making it achievable within 3 hours. it achievable within 3 hours.


Input Format

Depends on the menu item to be tested/used.


Constraints

Submissions have the following requirements:

Use a Stack to implement the undo feature.
Input validation: Ensure users enter valid options and handle errors gracefully.
Code should be modular, with separate functions for each operation.
Implement a Menu System for user interaction:
1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit


Output Format

Sample Run:

Welcome to Task Manager Simulator!
1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: 1
 
Enter task title: Finish report
Enter priority (1 = high, 2 = medium, 3 = low): 1
Enter time estimate (minutes): 60
Task added successfully!
 
Choose an option: 1
Enter task title: Buy groceries
Enter priority (1 = high, 2 = medium, 3 = low): 3
Enter time estimate (minutes): 30
Task added successfully!
 
Choose an option: 2
Tasks:
1. Finish report (Priority: High, Time: 60 mins)
2. Buy groceries (Priority: Low, Time: 30 mins)
 
Choose an option: 4
Last action undone successfully!
 
Choose an option: 5
Goodbye!
Sample Input 0

5
Sample Output 0

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
Sample Input 1

2
5
Sample Output 1

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
(No tasks to display)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
Sample Input 2

3
5
Sample Output 2

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: No tasks to complete.

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
Sample Input 3

1
Read journal
2
60
2
5
Sample Output 3

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
1. Read journal (Priority: Medium, Time: 60 mins)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
Sample Input 4

1
Finish report
1
60
1
Buy groceries
3
30
2
5
Sample Output 4

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
1. Finish report (Priority: High, Time: 60 mins)
2. Buy groceries (Priority: Low, Time: 30 mins)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
Sample Input 5

1
Homework
2
45
1
Project
1
120
2
3
Homework
2
5
Sample Output 5

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
1. Project (Priority: High, Time: 120 mins)
2. Homework (Priority: Medium, Time: 45 mins)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter the title of the task to complete: Task "Homework" completed successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
1. Project (Priority: High, Time: 120 mins)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
Sample Input 6

1
Write blog
2
50
4
2
5
Sample Output 6

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Last action undone successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
(No tasks to display)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
Sample Input 7

1
Laundry
3
15
1
Reading
2
60
3
Laundry
2
4
2
5
Sample Output 7

Welcome to Task Manager Simulator!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter task title: Enter priority (1 = high, 2 = medium, 3 = low): Enter time estimate (minutes): Task added successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Enter the title of the task to complete: Task "Laundry" completed successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
1. Reading (Priority: Medium, Time: 60 mins)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Last action undone successfully!

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Tasks:
1. Reading (Priority: Medium, Time: 60 mins)
2. Laundry (Priority: Low, Time: 15 mins)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
Choose an option: Goodbye!
