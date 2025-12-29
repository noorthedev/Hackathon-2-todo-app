from managers.todo_manager import TodoManager
from ui.console import ConsoleUI
from models.task import Task

def main():
    todo_manager = TodoManager()
    console_ui = ConsoleUI(todo_manager)
    console_ui.run()

if __name__ == "__main__":
    main()