---
id: 1
title: "Specify In-Memory TODO CRUD API"
stage: "spec"
date_iso: "2025-12-22"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "1-todo-crud-api"
branch: "1-todo-crud-api"
user: "user"
command: "/sp.specify"
labels: ["specification", "todo-api", "crud", "api-design"]
links:
  spec: "specs/1-todo-crud-api/spec.md"
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - "specs/1-todo-crud-api/spec.md"
  - "specs/1-todo-crud-api/checklists/requirements.md"
  - "history/prompts/1-todo-crud-api/1-specify-todo-crud-api.spec.prompt.md"
tests_yaml: |
  - "None"
---

# Specify In-Memory TODO CRUD API

## Prompt Text

```
/sp.specify

Project: In-Memory TODO CRUD API

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

Write this as a strict, unambiguous specification.
```

## Response Text

Created a complete technical specification for the In-Memory TODO CRUD API with:

1. Comprehensive user scenarios covering all API endpoints with priority levels (P1-P3)
2. Detailed functional requirements (FR-001 through FR-020) covering all specified endpoints and validation rules
3. Key entities definition for TODO Item and In-Memory Storage
4. Measurable success criteria (SC-001 through SC-006) focused on user outcomes
5. Edge cases handling for validation and error scenarios
6. Acceptance scenarios for each user story with Given/When/Then format

The specification follows the template structure and includes all required sections. A quality checklist was also created to validate the specification completeness.

## Outcome

Successfully created a complete, unambiguous technical specification for the In-Memory TODO CRUD API that covers all required endpoints, data model constraints, validation rules, and constraints as specified by the user.

## Evaluation

The specification meets all requirements with clear functional requirements, testable acceptance criteria, and measurable success outcomes. All user scenarios are covered with appropriate priority levels, and edge cases are identified. The specification is ready for the planning phase.