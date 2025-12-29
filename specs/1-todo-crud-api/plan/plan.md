# Implementation Plan: In-Memory TODO CRUD API

**Feature**: 1-todo-crud-api
**Created**: 2025-12-22
**Status**: Draft
**Author**: Claude
**Constitution Version**: 1.0.0

## Technical Context

### Knowns
- **Language**: Python (per constitution)
- **Framework**: FastAPI (per constitution)
- **Storage**: In-memory only (per constitution and spec)
- **Validation**: Pydantic models (per constitution)
- **API Style**: RESTful (per constitution)
- **Data Model**: TODO item with id, title, description, due_date, priority, completed
- **Endpoints**: GET /, POST/GET/PUT/PATCH/DELETE /todos/{id}, PATCH /todos/{id}/toggle
- **Response Format**: JSON only (per spec)

### Dependencies
- **FastAPI**: Web framework
- **Pydantic**: Data validation
- **uvicorn**: ASGI server
- **Python 3.8+**: Runtime environment

### Constraints
- In-memory storage only (data resets on restart)
- No external databases or files
- Title max 100 chars, required
- Description max 500 chars, optional
- Due date ISO format, today/future only
- Priority 1-5 range, default 3
- Completed boolean, default false
- Proper HTTP status codes (201, 200, 204, 400/422, 404)

### Assumptions
- Application will run as a single process
- No authentication required
- No concurrent access concerns for in-memory storage
- Simple auto-incrementing ID system

### Unknowns
- Specific Python version requirement (NEEDS CLARIFICATION)
- Deployment method details (NEEDS CLARIFICATION)

## Constitution Check

### Python FastAPI Standard
- All code will be written in Python using FastAPI
- Will leverage FastAPI's automatic API documentation (Swagger UI/Redoc)
- Will use async request handling where appropriate

### In-Memory Storage Only
- Will implement storage using Python data structures (dict, list)
- No database connections or file I/O
- Data will persist only in application memory

### Clean, Beginner-Friendly Code
- Will include clear docstrings for all functions/classes
- Will follow PEP 8 naming conventions
- Will avoid complex patterns that could confuse new developers

### Pydantic Validation
- All request/response data will use Pydantic models
- Will implement validation constraints as specified in requirements
- Will use type hints throughout

### RESTful API Conventions
- Will follow standard HTTP methods and resource naming
- Will implement proper URL patterns as specified

### HTTP Status Codes
- Will return 201 for creation, 200 for successful retrieval/updates, 204 for deletion
- Will return 400/422 for validation errors, 404 for missing resources

### Security Requirements
- Will not expose sensitive information in error messages
- Will return generic error messages that don't reveal internal details

### Development Workflow
- Will implement minimal viable solution without over-engineering
- Will focus on core functionality first, then add validation and error handling

## Research Phase (Phase 0)

### Task 0.1: Resolve Unknowns
**Decision**: Use Python 3.9+ for type hinting features and FastAPI compatibility
**Rationale**: Python 3.9+ provides better support for typing features like Union types and improved performance
**Alternatives considered**: Python 3.8 (still supported but older), Python 3.10+ (newer features but potentially less compatible)

**Decision**: Use uvicorn as the ASGI server for local development
**Rationale**: FastAPI's recommended server, simple to use, good for development and production
**Alternatives considered**: gunicorn (sync), daphne (for Django Channels), hypercorn (async alternative)

### Task 0.2: Best Practices Research
**FastAPI patterns**: Use Pydantic models for request/response validation, dependency injection for shared logic, async functions for endpoints
**Error handling**: Use FastAPI's exception handlers for consistent error responses
**In-memory storage**: Use a global dictionary with thread-safe operations if needed, auto-incrementing ID counter

## Design Phase (Phase 1)

### Task 1.1: Data Model Design
Create Pydantic models for:
- `TodoCreate`: Input validation for creating TODOs (title required, others optional)
- `TodoUpdate`: Input validation for updating TODOs (all fields optional)
- `TodoResponse`: Output model for API responses (all fields including ID)
- Global in-memory storage structure using Python dict

### Task 1.2: API Contract Design
Define endpoints with proper request/response models:
- GET / - Health check endpoint
- POST /todos - Create TODO with 201 status
- GET /todos - List all TODOs
- GET /todos/{id} - Get specific TODO
- PUT /todos/{id} - Update complete TODO
- PATCH /todos/{id} - Partial update
- DELETE /todos/{id} - Delete TODO
- PATCH /todos/{id}/toggle - Toggle completion status

### Task 1.3: Validation Strategy
Implement validation at multiple levels:
- Pydantic model validation for data format
- Custom validators for business rules (due date in future, priority range)
- FastAPI path parameter validation for ID format

## Implementation Phase (Phase 2)

### Task 2.1: Project Setup
1. Create requirements.txt with FastAPI and uvicorn
2. Create main.py file structure
3. Set up basic FastAPI app
4. Create directory structure for models, routes, storage

### Task 2.2: Data Models Implementation
1. Create Pydantic models for TODO item
2. Implement validation constraints (lengths, ranges, required fields)
3. Create in-memory storage structure

### Task 2.3: Core Storage Implementation
1. Implement in-memory storage class with auto-incrementing IDs
2. Implement create, read, update, delete operations
3. Implement toggle completion functionality

### Task 2.4: API Endpoints Implementation
1. Implement GET / endpoint (health check)
2. Implement POST /todos endpoint
3. Implement GET /todos endpoint
4. Implement GET /todos/{id} endpoint
5. Implement PUT /todos/{id} endpoint
6. Implement PATCH /todos/{id} endpoint
7. Implement DELETE /todos/{id} endpoint
8. Implement PATCH /todos/{id}/toggle endpoint

### Task 2.5: Error Handling Implementation
1. Create custom exception handlers
2. Implement proper HTTP status codes
3. Create consistent error response format

### Task 2.6: Validation Implementation
1. Add validation for title length (max 100 chars)
2. Add validation for description length (max 500 chars)
3. Add validation for due date (today or future)
4. Add validation for priority (1-5 range)

## Testing Phase (Phase 3)

### Task 3.1: Unit Testing
1. Test data model validation
2. Test storage operations
3. Test individual endpoint functionality

### Task 3.2: Integration Testing
1. Test full API workflows
2. Test error conditions and responses
3. Test edge cases

### Task 3.3: Manual Testing Checklist
- [ ] Start the application with `uvicorn main:app --reload`
- [ ] Verify API documentation at `/docs` and `/redoc`
- [ ] Test GET / endpoint returns health status
- [ ] Test POST /todos creates a TODO with valid data (201 status)
- [ ] Test POST /todos rejects invalid title (422 status)
- [ ] Test POST /todos rejects future-only due dates (422 status)
- [ ] Test POST /todos rejects invalid priority (422 status)
- [ ] Test GET /todos returns empty list when no items exist
- [ ] Test GET /todos returns list when items exist
- [ ] Test GET /todos/{id} returns specific item
- [ ] Test GET /todos/{id} returns 404 for non-existent ID
- [ ] Test PUT /todos/{id} updates complete item
- [ ] Test PUT /todos/{id} returns 404 for non-existent ID
- [ ] Test PATCH /todos/{id} updates partial item
- [ ] Test PATCH /todos/{id} returns 404 for non-existent ID
- [ ] Test DELETE /todos/{id} removes item (204 status)
- [ ] Test DELETE /todos/{id} returns 404 for non-existent ID
- [ ] Test PATCH /todos/{id}/toggle flips completion status
- [ ] Verify all responses are in JSON format
- [ ] Verify all endpoints return appropriate HTTP status codes

## Final Verification (Phase 4)

### Task 4.1: Compliance Verification
1. Verify all constitution principles are followed
2. Verify all specification requirements are implemented
3. Verify all functional requirements (FR-001 through FR-020) are met

### Task 4.2: Performance Verification
1. Verify API responds within acceptable time limits
2. Verify in-memory storage performs adequately
3. Verify no memory leaks exist

### Task 4.3: Documentation Verification
1. Verify API documentation is auto-generated correctly
2. Verify README includes local run instructions
3. Verify all code is properly documented

## Success Criteria Verification

- [ ] Users can create, read, update, and delete TODO items (SC-001)
- [ ] API responds within 500ms under normal conditions (SC-002)
- [ ] All validation rules properly enforced (SC-003)
- [ ] Appropriate HTTP status codes returned (SC-004)
- [ ] Application runs locally with simple setup (SC-005)
- [ ] All endpoints return valid JSON responses (SC-006)