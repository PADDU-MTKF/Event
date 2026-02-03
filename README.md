# 🌐 Event & User Management API

A **Django REST Framework (DRF) API** for managing **users and events**.  
Provides **CRUD operations** for user profiles and events, with **authentication via TOKEN**. Supports **image uploads** for event covers.

This API is designed to be used by frontend clients or other services.

---

## ✨ Features

- 🔐 **User authentication** via TOKEN
- 👤 **User profile management** (create, read, update, delete)
- 🎉 **Event management** with image uploads
- 📄 Full **CRUD support** for events
- 🧩 **Validation** for required fields and types
- 🛠️ Modular design (login, events, image storage)
- ⚡ RESTful API endpoints using **Django REST Framework**
- 🖼️ Handles **file uploads** (cover images) with automatic URL handling

---

## 🎯 Purpose

This API is designed to:

- Provide a secure backend for user registration and profile management
- Manage events with cover images and metadata
- Serve as a backend for web or mobile applications
- Maintain data integrity via **TOKEN-based authentication**

---

## 🗄️ Data Handling Notes

- User passwords are stored securely and **never returned** in API responses
- `TOKEN` is mandatory for **modifying or deleting** user and event data
- Authentication is token-based and validated per request
- Images are uploaded via a backend module and stored externally
- Uploaded images return a **publicly accessible URL** used in event records
- Input validations include:
  - Type checking (`int` for `phno` and `pincode`)
  - Mandatory field verification
  - Token and username validation for protected routes
- All database and file operations are handled through modular backend services

---

## 🛠️ Tech Stack

### Backend
- **Python**
- **Django REST Framework**
- **Appwrite** (Database & File Storage)


---


## 📚 API Endpoint Reference

| Endpoint                | Method | Headers Required        | Request Body / Params                                                                 | Description |
|-------------------------|--------|------------------------|--------------------------------------------------------------------------------------|-------------|
| `/`                     | GET    | None                   | None                                                                                 | Returns basic API status `{ "Status": "Ok" }` |
| `/api/login/`           | POST   | None                   | `{ "username": "john", "password": "secret123" }`                                    | Authenticate user and return `TOKEN` |
| `/api/user/`            | POST   | None                   | `{ "username": "john", "password": "secret123", "name": "John Doe", "phno": 9876543210 }` | Create a new user profile |
| `/api/user/`            | GET    | `TOKEN`                | `username` (query param)                                                             | Get user profile by username |
| `/api/user/`            | PUT    | `TOKEN`                | `{ "username": "john", "password": "secret123", "name": "John Doe", "phno": 9876543210 }` | Update user profile |
| `/api/user/`            | DELETE | `TOKEN`                | `{ "username": "john" }`                                                             | Delete user profile |
| `/api/event/`           | GET    | None                   | `page` (query param, optional, default=0)                                            | Get paginated list of events |
| `/api/event/`           | POST   | `TOKEN`, `USERNAME`    | Multipart/form-data: `title`, `description`, `startDate`, `endDate`, `coverImage` (file), `location`, `pincode` | Create a new event |
| `/api/event/`           | PUT    | `TOKEN`, `USERNAME`    | `{ "id": int, "title": "...", "description": "...", "startDate": "...", "endDate": "...", "coverImage": "...", "location": "...", "pincode": 123456 }` | Update existing event |
| `/api/event/`           | DELETE | `TOKEN`, `USERNAME`    | `{ "id": int, "coverImage": "url" }`                                                 | Delete an event |
| `/api/update-event/`    | POST   | `TOKEN`, `USERNAME`    | `{ "id": int, "title": "...", "description": "...", "startDate": "...", "endDate": "...", "coverImage": "...", "location": "...", "pincode": 123456 }` | Update existing event (alternative endpoint) |


