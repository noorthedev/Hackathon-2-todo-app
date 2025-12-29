# Quickstart Guide: In-Memory TODO CRUD API

**Feature**: 1-todo-crud-api
**Created**: 2025-12-22
**Status**: Complete

## Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)

### Installation
1. Clone or create the project directory
2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

### Running the Application
1. Create the main application file (main.py) with the TODO API implementation
2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
3. The API will be available at `http://localhost:8000`
4. API documentation will be available at `http://localhost:8000/docs`

### API Endpoints
- `GET /` - Health check
- `POST /todos` - Create a new TODO
- `GET /todos` - List all TODOs
- `GET /todos/{id}` - Get specific TODO
- `PUT /todos/{id}` - Update complete TODO
- `PATCH /todos/{id}` - Partial update
- `DELETE /todos/{id}` - Delete TODO
- `PATCH /todos/{id}/toggle` - Toggle completion status

### Example Usage
```bash
# Create a new TODO
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn FastAPI", "description": "Build a TODO app", "priority": 2}'

# Get all TODOs
curl http://localhost:8000/todos

# Get specific TODO
curl http://localhost:8000/todos/1

# Toggle completion status
curl -X PATCH http://localhost:8000/todos/1/toggle
```

### Stopping the Application
- Press `Ctrl+C` in the terminal where the server is running
- Note: All data will be lost when the application stops (in-memory storage only)