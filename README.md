To-Do List Manager CLI
===================================

Overview
--------

The To-Do List Manager is a command-line interface (CLI) application written in Python. It allows users to manage a to-do list by adding, viewing, and removing tasks. The application stores the tasks in a text file, allowing users to save their tasks for future sessions.

Features
--------

-   Add tasks to the to-do list.
-   View the list of tasks.
-   Remove tasks from the list.
-   Save tasks to a file for future use.

Prerequisites
-------------

-   Python installed on your computer.
-   A terminal or command prompt to run the CLI application.

How to Use
----------

1.  Run the Application

    Open your terminal or command prompt and navigate to the directory where the application script is located. Run the script using the command:
    
    ```bash
    python app.py
    ```
    

2.  Main Menu

    You will be presented with the following options:

    -   Add Task (Option 1): Enter a new task to add it to the to-do list.
    -   View Tasks (Option 2): Display the current list of tasks.
    -   Remove Task (Option 3): Remove a task from the list.
    -   Quit (Option 4): Save the tasks and exit the application.
3.  Add Task

    -   Choose option 1 from the main menu.
    -   Enter the description of the new task when prompted.
    -   The task will be added to the to-do list.
4.  View Tasks

    -   Choose option 2 from the main menu.
    -   The application will display the current list of tasks with a unique number for each task.
5.  Remove Task

    -   Choose option 3 from the main menu.
    -   Enter the number of the task you want to remove when prompted.
    -   The selected task will be removed from the list.
6.  Quit and Save

    -   Choose option 4 from the main menu when you are done.
    -   The to-do list will be saved to a text file (`todo_list.txt`) in the application directory.
    -   The application will exit.

Data Persistence
----------------

The application stores tasks in a text file called `todo_list.txt`. When you reopen the application, it loads the tasks from this file.

Error Handling
--------------

The application provides error handling for invalid input, ensuring a smooth user experience.