import sys
from typing import Optional
from managers.todo_manager import TodoManager
from models.task import Task

class ConsoleUI:
    def __init__(self, todo_manager: TodoManager):
        self.todo_manager = todo_manager
    
    def display_menu(self) -> None:
        print("\n===== MY TODO APP =====")
       print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Done")
        print("6. Mark Task Not Done")
        print("7. Exit Program")
        print("========================")
    
    def get_user_choice(self) -> str:
        return input("Enter your choice (1-7): ").strip()
    
    def get_task_details(self) -> tuple[str, str]:
        title = input("What do you need to do? : ").strip()
        description = input("Any extra details? (optional): ").strip()
        return title, description
    
    def get_task_id(self) -> Optional[int]:
        try:
            return int(input("Enter task number: ").strip())
        except ValueError:
            print("That's not a valid number!")
            return None
    
    def add_task(self) -> None:
        print("\n--- Adding New Task ---")
        title, description = self.get_task_details()
        
        if not title:
            print("You must enter what you need to do!")
            return
        
        task = self.todo_manager.add_task(title, description)
        print(f"Added! Task #{task.id}: {task.title}")
    
    def list_tasks(self) -> None:
        print("\n--- Your Tasks ---")
        tasks = self.todo_manager.list_tasks()
        
        if not tasks:
            print("No tasks yet! Add one to get started.")
            return
        
        pending_tasks = self.todo_manager.get_pending_tasks()
        if pending_tasks:
            print("\n📋 Things to do:")
            for task in pending_tasks:
                print(f"  {task}")
        
        completed_tasks = self.todo_manager.get_completed_tasks()
        if completed_tasks:
            print("\n✅ Completed tasks:")
            for task in completed_tasks:
                print(f"  {task}")
    
    def update_task(self) -> None:
        print("\n--- Editing Task ---")
        task_id = self.get_task_id()
        
        if task_id is None:
            return
        
        task = self.todo_manager.get_task(task_id)
        if not task:
            print(f"No task found with number {task_id}")
            return
        
        print(f"Current task: {task.title}")
        print(f"Current details: {task.description}")
        
        new_title = input("New task name (press Enter to keep current): ").strip()
        new_description = input("New details (press Enter to keep current): ").strip()
        
        if not new_title:
            new_title = None
        if not new_description:
            new_description = None
        
        if self.todo_manager.update_task(task_id, new_title, new_description):
            print("Task updated successfully!")
        else:
            print("Could not update task.")
    
    def delete_task(self) -> None:
        print("\n--- Deleting Task ---")
        task_id = self.get_task_id()
        
        if task_id is None:
            return
        
        task = self.todo_manager.get_task(task_id)
        if not task:
            print(f"No task found with number {task_id}")
            return
        
        confirm = input(f"Really delete '{task.title}'? (y/N): ").strip().lower()
        if confirm == 'y' or confirm == 'yes':
            if self.todo_manager.delete_task(task_id):
                print("Task deleted!")
            else:
                print("Could not delete task.")
        else:
            print("Deletion cancelled.")
    
    def mark_complete(self) -> None:
        print("\n--- Marking Task Done ---")
        task_id = self.get_task_id()
        
        if task_id is None:
            return
        
        if self.todo_manager.mark_complete(task_id):
            print("Task marked as done! ✅")
        else:
            print(f"No task found with number {task_id}")
    
    def mark_incomplete(self) -> None:
        print("\n--- Marking Task Not Done ---")
        task_id = self.get_task_id()
        
        if task_id is None:
            return
        
        if self.todo_manager.mark_incomplete(task_id):
            print("Task marked as not done! 📋")
        else:
            print(f"No task found with number {task_id}")
    
    def run(self) -> None:
        print("Welcome to My Todo App!")
        print("Let's get organized! 🚀")
        
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                self.update_task()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                self.mark_complete()
            elif choice == '6':
                self.mark_incomplete()
            elif choice == '7':
                print("Thanks for using My Todo App! See you next time! 👋")
                sys.exit(0)
            else:
                print("Please pick a number between 1 and 7!")
