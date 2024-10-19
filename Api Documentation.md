# Task Management API Documentation

## Base URL

```
http://localhost:8080/api/
```

## Authentication

All endpoints except for registration and login require a JWT token for authentication. You can obtain the token by logging in.

### Login

- **Endpoint:** `/login`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "user1",
    "password": "password123"
  }
  ```
- **Responses:**
  - **200 OK**: Token returned.
    ```json
    {
      "token": "your_jwt_token"
    }
    ```
  - **401 Unauthorized**: Invalid credentials.

## User Registration

### Register User

- **Endpoint:** `/register`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "username": "user1",
    "password": "password123"
  }
  ```
- **Responses:**
  - **201 Created**: User registered successfully.
  - **400 Bad Request**: Validation errors.

## Task Management

### Create Task

- **Endpoint:** `/tasks`
- **Method:** `POST`
- **Headers:**
  - `Authorization: Bearer your_jwt_token`
- **Request Body:**
  ```json
  {
    "title": "New Task",
    "description": "Task description",
    "status": "Todo",
    "priority": "High",
    "due_date": "2024-07-31"
  }
  ```
- **Responses:**
  - **201 Created**: Task created successfully.
  - **400 Bad Request**: Validation errors.

### Get All Tasks

- **Endpoint:** `/tasks`
- **Method:** `GET`
- **Headers:**
  - `Authorization: Bearer your_jwt_token`
- **Query Parameters:**
  - `status` (optional): Filter tasks by status (e.g., Todo, In Progress, Done).
  - `priority` (optional): Filter tasks by priority (e.g., High, Medium, Low).
  - `due_date` (optional): Filter tasks by due date.
  - `search` (optional): Search tasks by title or description.
- **Responses:**
  - **200 OK**: Returns a list of tasks.
    ```json
    [
      {
        "id": 1,
        "title": "New Task",
        "description": "Task description",
        "status": "Todo",
        "priority": "High",
        "due_date": "2024-07-31",
        "created_at": "2024-07-01T00:00:00Z",
        "updated_at": "2024-07-01T00:00:00Z",
        "user_id": 1
      }
    ]
    ```

### Update Task

- **Endpoint:** `/tasks/{taskId}`
- **Method:** `PUT`
- **Headers:**
  - `Authorization: Bearer your_jwt_token`
- **Request Body:**
  ```json
  {
    "title": "Updated Task",
    "description": "Updated description",
    "status": "In Progress",
    "priority": "Medium"
  }
  ```
- **Responses:**
  - **200 OK**: Task updated successfully.
  - **404 Not Found**: Task does not exist.
  - **400 Bad Request**: Validation errors.

### Delete Task

- **Endpoint:** `/tasks/{taskId}`
- **Method:** `DELETE`
- **Headers:**
  - `Authorization: Bearer your_jwt_token`
- **Responses:**
  - **204 No Content**: Task deleted successfully.
  - **404 Not Found**: Task does not exist.

## Status Codes

| Status Code | Description                                |
|-------------|--------------------------------------------|
| 200         | OK                                         |
| 201         | Created                                    |
| 204         | No Content                                 |
| 400         | Bad Request (Validation errors)            |
| 401         | Unauthorized (Invalid credentials)         |
| 404         | Not Found (Resource does not exist)       |
| 500         | Internal Server Error                      |

## Example Requests

### 1. User Registration

```bash
curl -X POST http://localhost:8080/api/register -H "Content-Type: application/json" -d '{"username": "user1", "password": "password123"}'
```

### 2. User Login

```bash
curl -X POST http://localhost:8080/api/login -H "Content-Type: application/json" -d '{"username": "user1", "password": "password123"}'
```

### 3. Create Task

```bash
curl -X POST http://localhost:8080/api/tasks -H "Authorization: Bearer your_jwt_token" -H "Content-Type: application/json" -d '{"title": "New Task", "description": "Task description", "status": "Todo", "priority": "High", "due_date": "2024-07-31"}'
```

### 4. Get All Tasks

```bash
curl -X GET http://localhost:8080/api/tasks -H "Authorization: Bearer your_jwt_token"
```

### 5. Update Task

```bash
curl -X PUT http://localhost:8080/api/tasks/1 -H "Authorization: Bearer your_jwt_token" -H "Content-Type: application/json" -d '{"title": "Updated Task", "description": "Updated description", "status": "In Progress", "priority": "Medium"}'
```

### 6. Delete Task

```bash
curl -X DELETE http://localhost:8080/api/tasks/1 -H "Authorization: Bearer your_jwt_token"
```

## Conclusion

This documentation provides an overview of the endpoints available in the Task Management API, along with examples of how to use them. For any issues or further questions, please refer to the codebase or reach out to the project maintainers.

---

Feel free to modify any part of this documentation to better match your project’s details or requirements!
