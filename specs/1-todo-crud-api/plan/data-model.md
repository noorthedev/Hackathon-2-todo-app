# Data Model: In-Memory TODO CRUD API

**Feature**: 1-todo-crud-api
**Created**: 2025-12-22
**Status**: Complete

## Entities

### TODO Item
**Description**: Represents a user's task to be completed

**Fields**:
- `id` (int): Auto-incrementing integer starting from 1, required, unique identifier
- `title` (str): Required, non-empty, trimmed, maximum 100 characters
- `description` (str | None): Optional, maximum 500 characters, default None
- `due_date` (datetime | None): Optional, ISO 8601 format, must be today or future, default None
- `priority` (int): Optional, integer between 1-5, default 3
- `completed` (bool): Boolean indicating completion status, default False

**Validation Rules**:
- `title`: Required, trimmed, non-empty, maximum 100 characters
- `description`: Optional, maximum 500 characters if provided
- `due_date`: Optional, must be today or future date if provided (ISO 8601 format)
- `priority`: Optional, must be integer between 1 and 5 if provided, default 3
- `completed`: Boolean, default False

## Storage Structure

### In-Memory Storage
**Description**: Temporary storage mechanism that holds TODO items in application memory

**Structure**:
- `todos` (dict[int, TODO Item]): Dictionary mapping ID to TODO item objects
- `next_id` (int): Counter for auto-incrementing ID generation, starts at 1

**Operations**:
- `create(todo: TODO Item) -> TODO Item`: Add new TODO item to storage, assign ID, return created item
- `read(id: int) -> TODO Item | None`: Retrieve TODO item by ID, return None if not found
- `read_all() -> list[TODO Item]`: Retrieve all TODO items
- `update(id: int, updates: dict) -> TODO Item | None`: Update TODO item by ID, return updated item or None if not found
- `delete(id: int) -> bool`: Delete TODO item by ID, return True if successful, False if not found
- `toggle_completion(id: int) -> TODO Item | None`: Toggle completion status of TODO item, return updated item or None if not found

## State Transitions

### Completion Status
- `completed = False` → `completed = True` (when toggled from incomplete)
- `completed = True` → `completed = False` (when toggled from complete)

## Relationships
- No relationships between TODO items (each item is independent)

## Constraints
- All data is stored in memory only (no persistence)
- Data is lost when application restarts
- ID uniqueness is maintained through auto-incrementing counter
- Title must be unique in terms of content (not enforced as a constraint in this implementation)