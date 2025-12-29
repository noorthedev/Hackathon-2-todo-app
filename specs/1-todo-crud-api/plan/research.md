# Research Document: In-Memory TODO CRUD API

**Feature**: 1-todo-crud-api
**Created**: 2025-12-22
**Status**: Complete

## Resolved Unknowns

### Unknown 1: Python Version Requirement

**Decision**: Use Python 3.9+
**Rationale**:
- FastAPI requires Python 3.7+ but works best with 3.9+
- Python 3.9+ provides better support for typing features like Union types (X | Y syntax)
- Better performance and memory management
- Good balance between features and compatibility
- Most cloud platforms support Python 3.9+

**Alternatives considered**:
- Python 3.8: Still supported but lacks newer typing features
- Python 3.10+: More advanced features but may have compatibility issues with some packages

### Unknown 2: Deployment Method Details

**Decision**: Use uvicorn for local development and simple deployment
**Rationale**:
- FastAPI's recommended ASGI server
- Simple command-line interface for development: `uvicorn main:app --reload`
- Can be used for production with proper configuration
- Lightweight and efficient
- Standard choice for FastAPI applications

**Alternatives considered**:
- gunicorn: More suitable for production but not necessary for this simple app
- hypercorn: Alternative ASGI server but less commonly used with FastAPI
- daphne: Used primarily with Django Channels

## Technology Best Practices

### FastAPI Patterns
- Use Pydantic models for request/response validation
- Implement async functions for endpoints to leverage FastAPI's async capabilities
- Use dependency injection for shared logic or database connections
- Leverage FastAPI's automatic API documentation (Swagger UI/Redoc)

### Error Handling
- Use FastAPI's exception handlers for consistent error responses
- Create custom exception classes for domain-specific errors
- Return consistent JSON error format with message and status code

### In-Memory Storage
- Use Python dictionary for O(1) access
- Use threading.Lock if concurrent access is needed (though not required for this basic implementation)
- Implement auto-incrementing ID using a simple counter
- Store all data in application memory with no persistence

### Validation Strategy
- Use Pydantic field validators for custom validation rules
- Implement custom validators for business rules (due date in future, priority range)
- Use FastAPI's built-in validation for path parameters (ID format)

## Implementation Approach

### Minimal Viable Solution
- Focus on core functionality first
- Implement basic CRUD operations
- Add validation and error handling iteratively
- Avoid over-engineering with unnecessary abstractions
- Keep the solution simple and beginner-friendly as required by constitution