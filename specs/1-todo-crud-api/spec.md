# Feature Specification: In-Memory TODO CRUD API

**Feature Branch**: `1-todo-crud-api`
**Created**: 2025-12-22
**Status**: Draft
**Input**: User description: "Project: In-Memory TODO CRUD API

Define a complete technical specification including:

1. API Endpoints
- GET /
- POST /todos
- GET /todos
- GET /todos/{id}
- PUT /todos/{id}
- PATCH /todos/{id}
- DELETE /todos/{id}
- PATCH /todos/{id}/toggle

2. Data Model
- id: auto-incrementing integer starting from 1
- title: required, trimmed, non-empty, max 100 chars
- description: optional, max 500 chars
- due_date: optional ISO datetime, today or future only
- priority: optional integer (1–5), default 3
- completed: boolean, default false

3. Validation Rules
- Reject invalid input with meaningful error messages
- Return 404 for missing resources
- Use 201, 200, 204, 400/422 appropriately

4. Constraints
- In-memory storage only
- Restarting the app resets data
- JSON responses only

5. Deliverables
- main.py with FastAPI app
- Clear API behavior description
- Ready to run locally

Write this as a strict, unambiguous specification."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Create TODO Item (Priority: P1)

A user wants to create a new TODO item with a title and optional details. They send a POST request to the /todos endpoint with the required information, and the system creates the item with a unique ID and returns the created item.

**Why this priority**: Creating TODO items is the core functionality that enables all other operations. Without this, the API has no value.

**Independent Test**: Can be fully tested by sending a POST request to /todos with valid data and verifying that a new TODO item is created with the correct attributes and a unique ID.

**Acceptance Scenarios**:

1. **Given** user has valid TODO data, **When** user sends POST request to /todos with required title, **Then** system returns 201 Created with the new TODO item including auto-generated ID
2. **Given** user has invalid TODO data (empty title), **When** user sends POST request to /todos, **Then** system returns 400/422 error with meaningful error message

---

### User Story 2 - Retrieve TODO Items (Priority: P1)

A user wants to view all their TODO items. They send a GET request to the /todos endpoint and receive a list of all TODO items.

**Why this priority**: Users need to be able to see their TODO items to manage them effectively.

**Independent Test**: Can be fully tested by creating some TODO items and then sending a GET request to /todos to verify that all items are returned in the response.

**Acceptance Scenarios**:

1. **Given** multiple TODO items exist, **When** user sends GET request to /todos, **Then** system returns 200 OK with list of all TODO items
2. **Given** no TODO items exist, **When** user sends GET request to /todos, **Then** system returns 200 OK with empty array

---

### User Story 3 - Retrieve Single TODO Item (Priority: P2)

A user wants to view details of a specific TODO item. They send a GET request to /todos/{id} with the item's ID and receive the specific item details.

**Why this priority**: Users need to access individual items to view or modify their details.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a GET request to /todos/{id} to verify that the specific item is returned.

**Acceptance Scenarios**:

1. **Given** a TODO item exists with ID, **When** user sends GET request to /todos/{id}, **Then** system returns 200 OK with the specific TODO item
2. **Given** no TODO item exists with the requested ID, **When** user sends GET request to /todos/{id}, **Then** system returns 404 Not Found

---

### User Story 4 - Update TODO Item (Priority: P2)

A user wants to update an existing TODO item. They send a PUT or PATCH request to /todos/{id} with updated information, and the system updates the item.

**Why this priority**: Users need to modify their TODO items as their plans change.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a PUT/PATCH request to update its attributes, verifying that the item is updated correctly.

**Acceptance Scenarios**:

1. **Given** a TODO item exists, **When** user sends PUT request to /todos/{id} with updated data, **Then** system returns 200 OK with updated TODO item
2. **Given** a TODO item exists, **When** user sends PATCH request to /todos/{id} with partial updated data, **Then** system returns 200 OK with updated TODO item
3. **Given** no TODO item exists with the requested ID, **When** user sends PUT/PATCH request to /todos/{id}, **Then** system returns 404 Not Found

---

### User Story 5 - Delete TODO Item (Priority: P2)

A user wants to remove a TODO item from their list. They send a DELETE request to /todos/{id} and the system removes the item.

**Why this priority**: Users need to be able to remove completed or irrelevant items from their list.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a DELETE request to /todos/{id}, verifying that the item is removed.

**Acceptance Scenarios**:

1. **Given** a TODO item exists, **When** user sends DELETE request to /todos/{id}, **Then** system returns 204 No Content and item is removed
2. **Given** no TODO item exists with the requested ID, **When** user sends DELETE request to /todos/{id}, **Then** system returns 404 Not Found

---

### User Story 6 - Toggle TODO Completion Status (Priority: P3)

A user wants to mark a TODO item as completed or incomplete. They send a PATCH request to /todos/{id}/toggle and the system flips the completion status.

**Why this priority**: Toggling completion status is a common operation that users perform frequently.

**Independent Test**: Can be fully tested by creating a TODO item and then sending a PATCH request to /todos/{id}/toggle, verifying that the completion status is flipped.

**Acceptance Scenarios**:

1. **Given** a TODO item exists with completed=false, **When** user sends PATCH request to /todos/{id}/toggle, **Then** system returns 200 OK with item's completed status changed to true
2. **Given** a TODO item exists with completed=true, **When** user sends PATCH request to /todos/{id}/toggle, **Then** system returns 200 OK with item's completed status changed to false

---

### User Story 7 - View API Home (Priority: P3)

A user wants to check if the API is running. They send a GET request to the root endpoint and receive a status response.

**Why this priority**: Basic health check functionality for the API.

**Independent Test**: Can be fully tested by sending a GET request to / and verifying that the API responds with appropriate status information.

**Acceptance Scenarios**:

1. **Given** API is running, **When** user sends GET request to /, **Then** system returns 200 OK with status information

---

### Edge Cases

- What happens when a user tries to create a TODO with a title longer than 100 characters? System should return 400/422 with meaningful error message.
- What happens when a user tries to create a TODO with a due date in the past? System should return 400/422 with meaningful error message.
- What happens when a user tries to create a TODO with a priority value outside the 1-5 range? System should return 400/422 with meaningful error message.
- What happens when a user tries to access a TODO with an invalid ID format? System should return 404 Not Found.
- What happens when the in-memory storage reaches capacity? System should handle gracefully with appropriate error responses.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a GET endpoint at / that returns API status information
- **FR-002**: System MUST provide a POST endpoint at /todos that creates a new TODO item with auto-incrementing ID
- **FR-003**: System MUST provide a GET endpoint at /todos that returns all TODO items
- **FR-004**: System MUST provide a GET endpoint at /todos/{id} that returns a specific TODO item by ID
- **FR-005**: System MUST provide a PUT endpoint at /todos/{id} that updates a complete TODO item
- **FR-006**: System MUST provide a PATCH endpoint at /todos/{id} that updates partial TODO item data
- **FR-007**: System MUST provide a DELETE endpoint at /todos/{id} that removes a TODO item
- **FR-008**: System MUST provide a PATCH endpoint at /todos/{id}/toggle that flips the completion status of a TODO item
- **FR-009**: System MUST validate that TODO title is required, trimmed, non-empty, and maximum 100 characters
- **FR-010**: System MUST validate that TODO description is optional and maximum 500 characters
- **FR-011**: System MUST validate that TODO due_date is optional ISO datetime and must be today or future only
- **FR-012**: System MUST validate that TODO priority is optional integer between 1 and 5, with default value of 3
- **FR-013**: System MUST validate that TODO completed is boolean with default value of false
- **FR-014**: System MUST reject invalid input with meaningful error messages using 400/422 status codes
- **FR-015**: System MUST return 404 status code for missing resources
- **FR-016**: System MUST use appropriate HTTP status codes: 201 for creation, 200 for successful retrieval/updates, 204 for successful deletion
- **FR-017**: System MUST use in-memory storage only with no external persistence
- **FR-018**: System MUST return JSON responses only for all endpoints
- **FR-019**: System MUST reset all data when the application restarts
- **FR-020**: System MUST provide auto-incrementing integer IDs starting from 1

### Key Entities *(include if feature involves data)*

- **TODO Item**: Represents a user's task to be completed, containing id, title, description, due_date, priority, and completed status
- **In-Memory Storage**: Temporary storage mechanism that holds TODO items in application memory with no persistence across restarts

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can create, read, update, and delete TODO items through the API with 100% success rate for valid requests
- **SC-002**: API responds to all requests within 500ms under normal load conditions
- **SC-003**: All validation rules are properly enforced with appropriate error messages returned for invalid input
- **SC-004**: API correctly returns appropriate HTTP status codes (201, 200, 204, 400/422, 404) for all scenarios
- **SC-005**: Application can be run locally with simple setup process (e.g., single command to start)
- **SC-006**: All endpoints return valid JSON responses that conform to expected data model structure