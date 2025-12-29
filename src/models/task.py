from datetime import datetime
from typing import Optional

class Task:
    def __init__(self, task_id: int, title: str, description: str = ""):
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def mark_complete(self) -> None:
        self.completed = True
        self.updated_at = datetime.now()
    
    def mark_incomplete(self) -> None:
        self.completed = False
        self.updated_at = datetime.now()
    
    def update(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.updated_at = datetime.now()
    
    def __str__(self) -> str:
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.id}: {self.title}"