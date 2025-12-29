# Todo App Constitution

## Core Principles

### Python FastAPI Standard
The project must be written in Python using FastAPI. All API endpoints must leverage FastAPI's built-in features including automatic API documentation generation, dependency injection, and asynchronous request handling where appropriate.

### In-Memory Storage Only
The application must use in-memory storage only (no database, no files). All data persistence is handled through memory structures with no external persistence mechanisms or file system dependencies.

### Clean, Beginner-Friendly Code
Code must be clean, readable, and beginner-friendly. All functions, classes, and modules must include clear documentation, follow consistent naming conventions, and avoid unnecessary complexity that could confuse new developers.

### Pydantic Validation
Use Pydantic models for all validation. All request/response data must be validated through Pydantic models with appropriate type hints and validation constraints.

### RESTful API Conventions
Follow RESTful API conventions strictly. All endpoints must follow standard HTTP methods (GET, POST, PUT, DELETE) and resource naming patterns with appropriate status codes.

### HTTP Status Codes
All API responses must use correct HTTP status codes. Success responses use appropriate 2xx codes, client errors use 4xx codes, and server errors use 5xx codes with clear error messages.

## Additional Constraints

The application must be easy to run locally with minimal setup. Dependencies should be kept to a minimum and installation should be straightforward through standard Python package managers.

## Security Requirements

Security-sensitive details must not be exposed. No sensitive information should be logged, returned in error messages, or stored in plain text. All error responses must be generic enough to not reveal internal system details.

## Development Workflow

No over-engineering; keep the solution simple and correct. Features should be implemented with the minimum viable approach that satisfies requirements without adding unnecessary complexity.

## Governance

This constitution defines the mandatory practices for this project. All code changes must comply with these principles. Deviations require explicit amendment to this constitution.

**Version**: 1.0.0 | **Ratified**: 2025-12-22 | **Last Amended**: 2025-12-22
