# Todo Console Application

A clean and user-friendly command-line Todo application built with Python.  
The application allows users to manage daily tasks through an interactive console interface.  
All tasks are stored **in memory**, so data is cleared when the program exits.

---

## Overview

The Todo Console Application provides a simple yet structured way to manage tasks directly from the terminal.  
Users can add, view, update, delete, and mark tasks as complete or incomplete using menu-driven input.

The program runs in a continuous loop and responds to user selections until the exit option is chosen.

This project is designed as a **foundational console application**, making it ideal for learning Python fundamentals and serving as a base for future enhancements such as APIs or web applications.

---

## Features

- **Add Task**  
  Create a new task by providing a title and an optional description.

- **View Task List**  
  Display all tasks with the following details:
  - Unique Task ID  
  - Completion Status (Complete / Incomplete)  
  - Task Title  
  - Task Description  

- **Update Task**  
  Modify the title or description of an existing task using its ID.

- **Delete Task**  
  Permanently remove a task from the list.

- **Mark as Complete / Incomplete**  
  Toggle the completion status of a task.

---

## Requirements

- Python **3.13** or higher

---

## How to Run

1. Navigate to the `src` directory:
   ```bash
   cd src


## Run the application:
python src/main.py

## Usage

Once the application starts, a menu will be displayed in the terminal.
The application continues running until the user chooses to exit.

## Menu options:

Option 1 – Add a new task
Option 2 – View all tasks
Option 3 – Update an existing task
Option 4 – Delete a task
Option 5 – Toggle task completion status
Option 6 – Exit the application
Enter the corresponding option number and follow the on-screen prompts to perform actions.



## Application Behavior

Tasks are stored only in memory

No database or file storage is used

All tasks are lost when the application exits

## Project Scope

- This application demonstrates:
- Python control flow
- User input handling
- In-memory data management
- CRUD operations via a console interface
- It can be extended into:
- A file-based or database-backed system
- A REST API using FastAPI
- A full-stack web application
- An AI-powered Todo assistant
