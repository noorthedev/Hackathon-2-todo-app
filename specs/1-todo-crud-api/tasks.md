# Implementation Tasks: In-Memory TODO CRUD API

**Feature**: 1-todo-crud-api
**Generated**: 2025-12-22
**Status**: Ready for Implementation

## Implementation Strategy

This implementation follows an incremental delivery approach with the following phases:
1. **Setup**: Project initialization and dependency management
2. **Foundational**: Core models and storage implementation (blocking prerequisites)
3. **User Stories**: Each user story implemented as a complete, independently testable increment
4. **Polish**: Cross-cutting concerns and final verification

MVP scope: User Story 1 (Create TODO Item) and User Story 2 (Retrieve TODO Items) with minimal validation.

## Dependencies

- **Python 3.9+**: Runtime environment
- **FastAPI**: Web framework
- **Pydantic**: Data validation
- **uvicorn**: ASGI server

### User Story Completion Order
1. US1: Create TODO Item (P1 priority)
2. US2: Retrieve TODO Items (P1 priority)
3. US3: Retrieve Single TODO Item (P2 priority)
4. US4: Update TODO Item (P2 priority)
5. US5: Delete TODO Item (P2 priority)
6. US6: Toggle TODO Completion Status (P3 priority)
7. US7: View API Home (P3 priority)

## Phase 1: Setup

### Goal
Initialize project structure and install dependencies.

- [X] T001 Create project directory structure: main.py, models/, services/, routes/
- [X] T002 Create requirements.txt with FastAPI, uvicorn dependencies
- [X] T003 Install dependencies using pip install -r requirements.txt
- [X] T004 Create basic main.py with FastAPI app initialization
- [X] T005 Test basic app startup with uvicorn main:app --reload

## Phase 2: Foundational

### Goal
Implement core data models and in-memory storage that will be used by all user stories.

- [X] T006 [P] Create TodoCreate Pydantic model in models/todo.py with validation for title (1-100 chars)
- [X] T007 [P] Create TodoUpdate Pydantic model in models/todo.py with validation constraints
- [X] T008 [P] Create TodoResponse Pydantic model in models/todo.py with all fields including ID
- [X] T009 [P] Create TodoPatch Pydantic model in models/todo.py for partial updates
- [X] T010 [P] Create InMemoryStorage class in services/storage.py with auto-incrementing ID
- [X] T011 [P] Implement create operation in InMemoryStorage class
- [X] T012 [P] Implement read operation in InMemoryStorage class
- [X] T013 [P] Implement read_all operation in InMemoryStorage class
- [X] T014 [P] Implement update operation in InMemoryStorage class
- [X] T015 [P] Implement delete operation in InMemoryStorage class
- [X] T016 [P] Implement toggle_completion operation in InMemoryStorage class
- [X] T017 [P] Create custom exception classes in models/exceptions.py for 404 and validation errors

## Phase 3: User Story 1 - Create TODO Item (P1)

### Goal
Enable users to create a new TODO item with a title and optional details.

**Independent Test**: Can be fully tested by sending a POST request to /todos with valid data and verifying that a new TODO item is created with the correct attributes and a unique ID.

- [X] T018 [US1] Implement POST /todos endpoint in routes/todos.py that accepts TodoCreate model
- [X] T019 [US1] Connect POST /todos endpoint to storage create operation
- [X] T020 [US1] Return 201 Created status with created TODO item
- [X] T021 [US1] Test POST /todos with valid data returns 201 and created item
- [X] T022 [US1] Implement validation for title length (max 100 chars)
- [X] T023 [US1] Implement validation for description length (max 500 chars)
- [X] T024 [US1] Implement validation for priority range (1-5)
- [X] T025 [US1] Implement validation for due date (today or future)
- [X] T026 [US1] Test POST /todos with invalid title returns 422 error
- [X] T027 [US1] Test POST /todos with invalid due date returns 422 error
- [X] T028 [US1] Test POST /todos with invalid priority returns 422 error

## Phase 4: User Story 2 - Retrieve TODO Items (P1)

### Goal
Enable users to view all their TODO items.

**Independent Test**: Can be fully tested by creating some TODO items and then sending a GET request to /todos to verify that all items are returned in the response.

- [X] T029 [US2] Implement GET /todos endpoint in routes/todos.py
- [X] T030 [US2] Connect GET /todos endpoint to storage read_all operation
- [X] T031 [US2] Return 200 OK with list of all TODO items
- [X] T032 [US2] Test GET /todos returns empty list when no items exist
- [X] T033 [US2] Test GET /todos returns list when items exist
- [X] T034 [US2] Verify response format matches TodoResponse model

## Phase 5: User Story 3 - Retrieve Single TODO Item (P2)

### Goal
Enable users to view details of a specific TODO item.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a GET request to /todos/{id} to verify that the specific item is returned.

- [X] T035 [US3] Implement GET /todos/{id} endpoint in routes/todos.py
- [X] T036 [US3] Add path parameter validation for ID (positive integer)
- [X] T037 [US3] Connect GET /todos/{id} endpoint to storage read operation
- [X] T038 [US3] Return 200 OK with specific TODO item
- [X] T039 [US3] Return 404 Not Found for non-existent ID
- [X] T040 [US3] Test GET /todos/{id} returns specific item when it exists
- [X] T041 [US3] Test GET /todos/{id} returns 404 for non-existent ID

## Phase 6: User Story 4 - Update TODO Item (P2)

### Goal
Enable users to update an existing TODO item.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a PUT/PATCH request to update its attributes, verifying that the item is updated correctly.

- [X] T042 [US4] Implement PUT /todos/{id} endpoint in routes/todos.py that accepts TodoUpdate model
- [X] T043 [US4] Connect PUT /todos/{id} endpoint to storage update operation
- [X] T044 [US4] Return 200 OK with updated TODO item
- [X] T045 [US4] Return 404 Not Found for non-existent ID
- [X] T046 [US4] Test PUT /todos/{id} updates complete item
- [X] T047 [US4] Test PUT /todos/{id} returns 404 for non-existent ID
- [X] T048 [US5] Implement PATCH /todos/{id} endpoint in routes/todos.py that accepts TodoPatch model
- [X] T049 [US5] Connect PATCH /todos/{id} endpoint to storage update operation
- [X] T050 [US5] Return 200 OK with updated TODO item
- [X] T051 [US5] Return 404 Not Found for non-existent ID
- [X] T052 [US5] Test PATCH /todos/{id} updates partial item
- [X] T053 [US5] Test PATCH /todos/{id} returns 404 for non-existent ID

## Phase 7: User Story 5 - Delete TODO Item (P2)

### Goal
Enable users to remove a TODO item from their list.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a DELETE request to /todos/{id}, verifying that the item is removed.

- [X] T054 [US5] Implement DELETE /todos/{id} endpoint in routes/todos.py
- [X] T055 [US5] Connect DELETE /todos/{id} endpoint to storage delete operation
- [X] T056 [US5] Return 204 No Content on successful deletion
- [X] T057 [US5] Return 404 Not Found for non-existent ID
- [X] T058 [US5] Test DELETE /todos/{id} removes item and returns 204
- [X] T059 [US5] Test DELETE /todos/{id} returns 404 for non-existent ID

## Phase 8: User Story 6 - Toggle TODO Completion Status (P3)

### Goal
Enable users to mark a TODO item as completed or incomplete.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a PATCH request to /todos/{id}/toggle, verifying that the completion status is flipped.

- [X] T060 [US6] Implement PATCH /todos/{id}/toggle endpoint in routes/todos.py
- [X] T061 [US6] Connect PATCH /todos/{id}/toggle endpoint to storage toggle_completion operation
- [X] T062 [US6] Return 200 OK with updated TODO item
- [X] T063 [US6] Return 404 Not Found for non-existent ID
- [X] T064 [US6] Test PATCH /todos/{id}/toggle changes completed status from false to true
- [X] T065 [US6] Test PATCH /todos/{id}/toggle changes completed status from true to false
- [X] T066 [US6] Test PATCH /todos/{id}/toggle returns 404 for non-existent ID

## Phase 9: User Story 7 - View API Home (P3)

### Goal
Provide a health check endpoint for the API.

**Independent Test**: Can be fully tested by sending a GET request to / and verifying that the API responds with appropriate status information.

- [X] T067 [US7] Implement GET / endpoint in main.py for health check
- [X] T068 [US7] Return 200 OK with status information
- [X] T069 [US7] Test GET / returns health status response
- [X] T070 [US7] Verify API documentation is available at /docs and /redoc

## Phase 10: Polish & Cross-Cutting Concerns

### Goal
Implement error handling, validation, and verification across the entire API.

- [X] T071 Implement global exception handler for consistent error responses
- [X] T072 Create ErrorResponse Pydantic model for consistent error format
- [X] T073 Return 400/422 for validation errors with meaningful messages
- [X] T074 Return 404 for missing resources with meaningful messages
- [X] T075 Ensure all responses use JSON format
- [X] T076 Verify all endpoints return appropriate HTTP status codes (201, 200, 204, 400/422, 404)
- [X] T077 Add docstrings to all functions and classes for beginner-friendliness
- [X] T078 Verify no sensitive information is exposed in error messages
- [X] T079 Test that in-memory storage resets on application restart
- [X] T080 Verify all functional requirements (FR-001 through FR-020) are implemented
- [X] T081 Run complete manual testing checklist
- [X] T082 Verify all success criteria (SC-001 through SC-006) are met

## Parallel Execution Examples

The following tasks can be executed in parallel as they work on different files/components:
- T006-T009: All model creation tasks in models/todo.py
- T011-T016: All storage operations in services/storage.py
- T018, T029, T035: Different endpoints in routes/todos.py
- T042, T048, T054: Different HTTP methods in routes/todos.py

## MVP Scope (Minimum Viable Product)

The MVP includes:
- Tasks T001-T017 (Setup and Foundational)
- Tasks T018-T028 (User Story 1 - Create TODO)
- Tasks T029-T034 (User Story 2 - Retrieve TODOs)

This provides a working API with core CRUD functionality that can create and retrieve TODO items with proper validation.