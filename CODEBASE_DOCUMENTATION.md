# 📚 Mini PMS - Complete Codebase Documentation

**Project:** Mini Project Management System  
**Author:** Kushagra Bhardwaj (@Kush05Bhardwaj)  
**License:** MIT  
**Last Updated:** February 23, 2026  

---

## 📑 Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture & Tech Stack](#architecture--tech-stack)
3. [Directory Structure](#directory-structure)
4. [Core Application Files](#core-application-files)
5. [Authentication Module](#authentication-module)
6. [Teams Module](#teams-module)
7. [Documents Module](#documents-module)
8. [Evaluations Module](#evaluations-module)
9. [UI Routes Module](#ui-routes-module)
10. [Frontend Templates](#frontend-templates)
11. [Configuration & Environment](#configuration--environment)
12. [Database Schema](#database-schema)
13. [API Endpoints Summary](#api-endpoints-summary)
14. [Security Features](#security-features)
15. [Deployment Files](#deployment-files)
16. [Issues & Recommendations](#issues--recommendations)

---

## 🎯 Project Overview

**Mini PMS** is a role-based project management system built with Flask and MongoDB. It facilitates collaboration between three user roles:

- **Students:** Upload project documents and view evaluations
- **Mentors:** Review documents and submit team evaluations
- **Admins:** Create teams, assign users, and monitor the entire system

### Key Features
- JWT-based authentication with cookie support
- Role-based access control (RBAC)
- Document upload with file validation
- Team-specific document organization
- Evaluation/grading system
- Modern responsive UI with AJAX interactions

---

## 🏗️ Architecture & Tech Stack

### Backend
- **Framework:** Flask 3.1.2
- **Database:** MongoDB (via pymongo 4.16.0)
- **Authentication:** Flask-JWT-Extended 4.7.1, PyJWT 2.10.1
- **Password Hashing:** Werkzeug (built-in)
- **Environment:** python-dotenv 1.2.1

### Frontend
- **Templating:** Jinja2 3.1.6
- **JavaScript:** Vanilla ES6+ (Fetch API, async/await)
- **CSS:** Custom CSS3 with gradients and flexbox/grid
- **No external CSS framework** (fully custom styling)

### DevOps
- **Containerization:** Docker
- **Python Version:** 3.10

### Dependencies (requirements.txt)
```
blinker==1.9.0
click==8.3.1
colorama==0.4.6
dnspython==2.8.0
Flask==3.1.2
Flask-JWT-Extended==4.7.1
itsdangerous==2.2.0
Jinja2==3.1.6
MarkupSafe==3.0.3
PyJWT==2.10.1
pymongo==4.16.0
python-dotenv==1.2.1
Werkzeug==3.1.5
```

---

## 📂 Directory Structure

```
mini_pms/
│
├── 📄 main.py                      # Application entry point
├── 📄 requirements.txt             # Python dependencies
├── 📄 Dockerfile                   # Docker container configuration
├── 📄 docker-compoee.yml           # Docker Compose file (EMPTY)
├── 📄 LICENSE                      # MIT License
├── 📄 README.md                    # Project documentation
├── 📄 .env                         # Environment variables (MongoDB URI, secrets)
│
├── 📁 app/                         # Main application package
│   ├── 📄 __init__.py              # Flask app factory
│   ├── 📄 config.py                # Configuration class
│   ├── 📄 db.py                    # MongoDB connection utilities
│   ├── 📄 email.py                 # Email simulation utility
│   ├── 📄 local_cache.py           # Simple in-memory cache
│   ├── 📄 logger.py                # Logging configuration
│   │
│   ├── 📁 auth/                    # Authentication module
│   │   ├── 📄 models.py            # User model
│   │   ├── 📄 routes.py            # Login/register endpoints
│   │   ├── 📄 utils.py             # Role-based decorators
│   │   └── 📄 ui_protect.py        # UI route protection (unused)
│   │
│   ├── 📁 teams/                   # Team management module
│   │   ├── 📄 models.py            # Team model
│   │   └── 📄 routes.py            # Team CRUD endpoints
│   │
│   ├── 📁 documents/               # Document management module
│   │   ├── 📄 models.py            # Document model
│   │   └── 📄 routes.py            # Upload/review endpoints
│   │
│   ├── 📁 evaluations/             # Evaluation module
│   │   ├── 📄 models.py            # Evaluation model
│   │   └── 📄 routes.py            # Evaluation endpoints
│   │
│   ├── 📁 ui/                      # Web UI routes
│   │   └── 📄 routes.py            # Dashboard routes (login, student, mentor, admin)
│   │
│   └── 📁 frontend/                # Legacy templates (Bootstrap-based)
│       ├── 📄 base.html            # Old base template
│       ├── 📄 admin_dashboard.html # Old admin template
│       ├── 📄 mentor_dashboard.html
│       ├── 📄 student_dashboard.html
│       └── 📄 login.html
│
├── 📁 frontend/                    # Active templates (Custom CSS)
│   ├── 📄 base.html                # Base template with nav
│   ├── 📄 login.html               # Login page
│   ├── 📄 dashboard_student.html   # Student dashboard
│   ├── 📄 dashboard_mentor.html    # Mentor dashboard
│   └── 📄 dashboard_admin.html     # Admin dashboard
│
├── 📁 uploads/                     # File storage
│   └── 📁 teams/                   # Team-specific folders
│       └── [TeamName]/             # Created dynamically
│
└── 📁 tests/                       # Test directory (empty)
```

---

## 🔧 Core Application Files

### `main.py` - Application Entry Point
**Purpose:** Starts the Flask development server  
**Lines of Code:** 6

```python
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**Key Points:**
- Imports app factory from `app/__init__.py`
- Runs on all interfaces (`0.0.0.0`) for Docker compatibility
- Debug mode enabled (should be disabled in production)
- Port 5000 (standard Flask port)

---

### `app/__init__.py` - Flask App Factory
**Purpose:** Creates and configures the Flask application  
**Lines of Code:** 33

**Functionality:**
- Initializes JWTManager for authentication
- Sets up logging
- Registers all blueprints (auth, teams, documents, evaluations, ui)
- Configures template folder to use `frontend/` directory
- Defines error handlers (404, 500)

**Blueprints Registered:**
1. `auth_bp` - `/auth/*` routes
2. `teams_bp` - `/teams/*` routes
3. `documents_bp` - `/documents/*` routes
4. `evaluations_bp` - `/evaluations/*` routes
5. `ui_bp` - Root level routes (`/`, `/login`, `/student`, etc.)

**Error Handlers:**
- **404:** Returns `{"message": "Resource not found"}`
- **500:** Returns `{"message": "Internal server error"}`

---

### `app/config.py` - Configuration
**Purpose:** Centralized configuration using environment variables  
**Lines of Code:** 11

**Configuration Variables:**
| Variable | Default | Description |
|----------|---------|-------------|
| `SECRET_KEY` | `'secret-key'` | Flask session encryption key |
| `MONGO_URI` | `'mongodb://localhost:27017/mini_pms'` | MongoDB connection string |
| `JWT_SECRET_KEY` | `'jwt-secret-key'` | JWT token signing key |
| `JWT_TOKEN_LOCATION` | `['headers', 'cookies']` | Where to look for JWT tokens |
| `JWT_COOKIE_SECURE` | `False` | HTTPS-only cookies (prod: True) |
| `JWT_COOKIE_CSRF_PROTECT` | `False` | CSRF protection for cookies |
| `ENV` | `"dev"` | Environment identifier |

**Security Note:** Uses `.env` file via `python-dotenv` for sensitive data

---

### `app/db.py` - Database Connection
**Purpose:** MongoDB connection management  
**Lines of Code:** 12

**Functions:**

#### `get_db()`
- Returns MongoDB database instance
- Uses Flask's `g` object to store connection per request
- Automatically extracts database name from `MONGO_URI`

#### `get_user_by_email(email)`
- Helper function to find user by email
- Returns user document or `None`
- Used by authentication routes

**Connection Pattern:**
```python
from app.db import get_db
db = get_db()
users = db.users.find_one({"email": "test@example.com"})
```

---

### `app/email.py` - Email Utility
**Purpose:** Email simulation (prints to console)  
**Lines of Code:** 5

**Functionality:**
- Simulates email sending for development
- Prints recipient, subject, and body to console
- **Not production-ready** - needs SMTP integration

**Usage Example:**
```python
send_email("user@example.com", "Welcome!", "Your account is ready")
```

---

### `app/local_cache.py` - Simple Cache
**Purpose:** In-memory key-value cache  
**Lines of Code:** 7

**Functions:**
- `get(key)` - Retrieve cached value
- `set(key, value, ttl=None)` - Store value (TTL not implemented)

**Limitations:**
- No TTL (time-to-live) implementation
- Cache cleared on app restart
- Not thread-safe
- **Recommendation:** Use Redis for production

**Usage in Code:**
- Referenced in `documents/routes.py` but not actively used
- Commented out code shows intent for caching mentor documents

---

### `app/logger.py` - Logging Setup
**Purpose:** Configures application logging  
**Lines of Code:** 6

**Configuration:**
- Log level: `INFO`
- Format: `%(asctime)s - %(name)s - %(levelname)s - %(message)s`
- Logger name: `mini_pms`

**Usage:**
```python
from app.logger import setup_logger
logger = setup_logger()
logger.info("Application started")
```

---

## 🔐 Authentication Module

### `app/auth/models.py` - User Model
**Lines of Code:** 9

**Class: User**

**Attributes:**
- `email` (str) - User's email address (unique identifier)
- `password_hash` (str) - Bcrypt-hashed password
- `role` (str) - One of: `'Admin'`, `'Mentor'`, `'Student'`

**Methods:**

#### `__init__(self, email, password, role='Student')`
- Hashes password using `werkzeug.security.generate_password_hash()`
- Default role: Student

#### `check_password(self, password)`
- Verifies password against stored hash
- Uses `werkzeug.security.check_password_hash()`
- Returns: `True` or `False`

**Security:**
- Passwords never stored in plaintext
- Uses Werkzeug's PBKDF2 hashing (industry standard)

---

### `app/auth/routes.py` - Authentication Endpoints
**Lines of Code:** 46

**Blueprint:** `auth_bp` (URL prefix: `/auth`)

#### `POST /auth/register`
**Purpose:** Create new user account

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123",
  "role": "Student"  // Optional, defaults to "Student"
}
```

**Validations:**
- Password must be ≥6 characters
- Role must be: `Admin`, `Mentor`, or `Student`
- Email must be unique

**Responses:**
- **201:** User registered successfully
- **400:** Validation error or user exists

---

#### `POST /auth/login`
**Purpose:** Authenticate user and get JWT token

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Responses:**
- **200:** Returns JWT token
  ```json
  {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
  ```
- **401:** Invalid credentials

**Token Claims:**
- `identity` - User's email
- `role` - User's role (additional claim)

**Usage:**
```bash
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

---

### `app/auth/utils.py` - Authorization Decorator
**Lines of Code:** 13

**Function: `role_required(required_role)`**

**Purpose:** Protect API endpoints by role

**Usage:**
```python
@app.route('/admin-only')
@jwt_required()
@role_required("admin")
def admin_endpoint():
    return {"message": "Admin access granted"}
```

**Functionality:**
1. Verifies JWT token exists
2. Extracts `role` claim from token
3. Compares with required role
4. Returns 403 if roles don't match

**Roles:** `"admin"`, `"mentor"`, `"student"` (case-sensitive)

---

### `app/auth/ui_protect.py` - UI Route Protection (UNUSED)
**Lines of Code:** 11

**Status:** ⚠️ Not actively used in current codebase

**Original Intent:** Protect web UI routes (similar to `role_required`)

**Why Unused:**
- UI routes use `role_required` from `utils.py` instead
- Redirects to `/ui/login` instead of returning JSON
- Kept for potential future use

---

## 👥 Teams Module

### `app/teams/models.py` - Team Model
**Lines of Code:** 6

**Class: Team**

**Attributes:**
- `name` (str) - Team name (unique identifier)
- `mentor_email` (str) - Email of assigned mentor
- `students` (list) - List of student email addresses
- `status` (str) - Team status (default: `"active"`)

**Constructor:**
```python
team = Team("Team Alpha", "mentor@example.com")
```

**Database Representation:**
```json
{
  "name": "Team Alpha",
  "mentor_email": "mentor@example.com",
  "students": ["student1@example.com", "student2@example.com"],
  "status": "active"
}
```

---

### `app/teams/routes.py` - Team Management Endpoints
**Lines of Code:** 72

**Blueprint:** `teams_bp` (URL prefix: `/teams`)

---

#### `POST /teams/create`
**Access:** Admin only  
**Purpose:** Create a new team

**Request Body:**
```json
{
  "name": "Team Alpha",
  "mentor_email": "mentor@example.com"
}
```

**Responses:**
- **201:** Team created successfully
- **400:** Missing required fields
- **403:** Not an admin

**Implementation:**
```python
@teams_bp.route('/create', methods=['POST'])
@jwt_required()
@role_required("admin")
def create_team():
    # Creates team with empty students list
```

---

#### `POST /teams/add-student`
**Access:** Admin only  
**Purpose:** Add a student to an existing team

**Request Body:**
```json
{
  "team_name": "Team Alpha",
  "student_email": "student@example.com"
}
```

**Responses:**
- **200:** Student added successfully
- **404:** Team not found or student already in team
- **400:** Missing required fields

**Database Operation:**
```python
db.teams.update_one(
    {"name": team_name},
    {"$addToSet": {"students": student_email}}  # Prevents duplicates
)
```

---

#### `GET /teams/my-team`
**Access:** Student only  
**Purpose:** Get the team a student belongs to

**Response:**
```json
{
  "name": "Team Alpha",
  "mentor_email": "mentor@example.com",
  "students": ["student1@example.com", "student2@example.com"],
  "status": "active"
}
```

**Implementation:**
```python
email = get_jwt_identity()  # Gets student's email from JWT
team = db.teams.find_one({"students": email})
```

---

#### `GET /teams/my-teams`
**Access:** Mentor only  
**Purpose:** Get all teams assigned to a mentor

**Response:**
```json
[
  {
    "name": "Team Alpha",
    "mentor_email": "mentor@example.com",
    "students": ["student1@example.com"],
    "status": "active"
  },
  {
    "name": "Team Beta",
    "mentor_email": "mentor@example.com",
    "students": ["student2@example.com"],
    "status": "active"
  }
]
```

---

#### `GET /teams/all`
**Access:** Admin only  
**Purpose:** Get all teams in the system

**Response:** Array of all team objects

---

## 📄 Documents Module

### `app/documents/models.py` - Document Model
**Lines of Code:** 8

**Class: Document**

**Attributes:**
- `filename` (str) - Unique filename (UUID-based)
- `uploaded_by` (str) - Student's email
- `team_name` (str) - Team the document belongs to
- `status` (str) - One of: `"pending"`, `"approved"`, `"rejected"`
- `uploaded_at` (datetime) - Upload timestamp (UTC)
- `review_comment` (str|None) - Mentor's review comment

**Initial State:**
- All documents start with status: `"pending"`
- `review_comment` is `None` until reviewed

---

### `app/documents/routes.py` - Document Management Endpoints
**Lines of Code:** 105

**Blueprint:** `documents_bp` (URL prefix: `/documents`)

**Configuration:**
- `UPLOAD_FOLDER` = `"uploads"`
- `ALLOWED_EXTENSIONS` = `{"pdf", "png", "jpg", "jpeg", "docx"}`
- `MAX_FILE_SIZE` = 5 MB

---

#### `POST /documents/upload`
**Access:** Student only  
**Purpose:** Upload a project document

**Request:** Multipart form data
- `file` - File upload field

**Validation:**
1. File must be present
2. File extension must be in allowed list
3. File size must be ≤5 MB
4. Student must belong to a team

**File Storage:**
- Path: `uploads/teams/[TeamName]/[UUID].[extension]`
- Filename: UUID v4 for uniqueness
- Original filename discarded for security

**Example:**
```
uploads/teams/Team Alpha/3f8b9c1e-4a5d-6f7e-8g9h-0i1j2k3l4m5n.pdf
```

**Responses:**
- **201:** File uploaded successfully
  ```json
  {
    "msg": "File uploaded",
    "status": "pending"
  }
  ```
- **400:** No file, invalid type, or size exceeded
- **400:** Student not in any team

**Security Measures:**
1. UUID filenames prevent path traversal
2. File extension whitelist
3. Size limit enforcement
4. Team-specific folders isolate access

---

#### `GET /documents/mentor/docs`
**Access:** Mentor only  
**Purpose:** View documents from mentor's teams

**Query Parameters:**
- `page` (default: 1) - Page number
- `per_page` (default: 10) - Items per page

**Response:**
```json
[
  {
    "filename": "uuid.pdf",
    "team_name": "Team Alpha",
    "uploaded_by": "student@example.com",
    "status": "pending",
    "uploaded_at": "2026-02-23T10:30:00Z",
    "review_comment": null
  }
]
```

**Implementation:**
```python
# Find all teams mentored by user
teams = db.teams.find({"mentor_email": email})
team_names = [t["name"] for t in teams]

# Find documents from those teams
docs = db.documents.find({"team_name": {"$in": team_names}})
```

**Pagination:**
```python
.skip((page - 1) * per_page).limit(per_page)
```

**Note:** Cache implementation commented out but not active

---

#### `POST /documents/review`
**Access:** Mentor only  
**Purpose:** Approve or reject a document

**Request Body:**
```json
{
  "filename": "uuid.pdf",
  "status": "approved",  // or "rejected"
  "comment": "Good work!"
}
```

**Database Update:**
```python
db.documents.update_one(
    {"filename": filename},
    {"$set": {"status": status, "review_comment": comment}}
)
```

**Responses:**
- **200:** `{"msg": "Document approved/rejected"}`

**Issue:** ⚠️ No validation that mentor owns the document's team

---

## 📊 Evaluations Module

### `app/evaluations/models.py` - Evaluation Model
**Lines of Code:** 8

**Class: Evaluation**

**Attributes:**
- `team_name` (str) - Team being evaluated
- `mentor_email` (str) - Mentor who submitted evaluation
- `marks` (int/float) - Score out of 100
- `remarks` (str) - Written feedback
- `created_at` (datetime) - Evaluation timestamp (UTC)

**Database Representation:**
```json
{
  "team_name": "Team Alpha",
  "mentor_email": "mentor@example.com",
  "marks": 85,
  "remarks": "Excellent work on the frontend design",
  "created_at": "2026-02-23T15:45:00Z"
}
```

---

### `app/evaluations/routes.py` - Evaluation Endpoints
**Lines of Code:** 51

**Blueprint:** `evaluations_bp` (URL prefix: `/evaluations`)

---

#### `POST /evaluations/submit`
**Access:** Mentor only  
**Purpose:** Submit evaluation for a team

**Request Body:**
```json
{
  "team_name": "Team Alpha",
  "marks": 85,
  "remarks": "Great work!"
}
```

**Validation:**
- Mentor must be assigned to the team
- Returns 403 if not authorized

**Implementation:**
```python
# Verify mentor owns the team
team = db.teams.find_one({"name": team_name, "mentor_email": email})
if not team:
    return jsonify({"msg": "Unauthorized team"}), 403
```

**Responses:**
- **201:** Evaluation submitted
- **403:** Unauthorized team

**Issue:** ⚠️ No validation for marks range (should be 0-100)

---

#### `GET /evaluations/my-result`
**Access:** Student only  
**Purpose:** View evaluation for student's team

**Response:**
```json
{
  "team_name": "Team Alpha",
  "mentor_email": "mentor@example.com",
  "marks": 85,
  "remarks": "Great work!",
  "created_at": "2026-02-23T15:45:00Z"
}
```

**Implementation:**
```python
# Find student's team
team = db.teams.find_one({"students": email})

# Find evaluation for that team
evaluation = db.evaluations.find_one({"team_name": team["name"]})
```

**Responses:**
- **200:** Returns evaluation
- **404:** No team found

---

#### `GET /evaluations/all`
**Access:** Admin only  
**Purpose:** View all evaluations in the system

**Response:** Array of all evaluation objects

**Use Case:** Administrative oversight, analytics

---

## 🖥️ UI Routes Module

### `app/ui/routes.py` - Web Interface Routes
**Lines of Code:** 95

**Blueprint:** `ui_bp` (No URL prefix - root level routes)

---

#### `GET /`
**Access:** Public  
**Purpose:** Root redirect

**Behavior:** Redirects to `/login`

---

#### `GET/POST /login`
**Access:** Public  
**Purpose:** User login page

**GET Request:**
- Renders login form (`login.html`)

**POST Request:**
- Form data: `email`, `password`
- Validates credentials
- Creates JWT token
- Sets token as cookie (`access_token_cookie`)
- Redirects to role-specific dashboard:
  - Student → `/student`
  - Mentor → `/mentor`
  - Admin → `/admin`

**Password Verification:**
```python
from app.auth.models import User
temp_user = User(user["email"], user["password_hash"])
temp_user.password_hash = user["password_hash"]
temp_user.check_password(password)  # Verifies against hash
```

**Cookie Setup:**
```python
response.set_cookie('access_token_cookie', access_token)
```

**Error Handling:**
- Renders `login.html` with error message on failure

---

#### `GET /student`
**Access:** Student only (JWT + role check)  
**Purpose:** Student dashboard

**Data Provided:**
1. **Team Information:** Student's team details
2. **Documents:** All documents uploaded by the team
3. **Evaluation:** Team's evaluation result (if exists)

**Template Context:**
```python
{
  "team": {"name": "...", "mentor_email": "...", "students": [...]},
  "docs": [{"filename": "...", "status": "...", ...}],
  "result": {"marks": 85, "remarks": "...", ...}
}
```

**Features:**
- Upload documents via AJAX
- View document approval status
- View evaluation results

---

#### `GET /mentor`
**Access:** Mentor only (JWT + role check)  
**Purpose:** Mentor dashboard

**Data Provided:**
1. **Teams:** All teams assigned to mentor
2. **Documents:** All documents from mentor's teams

**Template Context:**
```python
{
  "teams": [{"name": "...", ...}],
  "docs": [{"filename": "...", "team_name": "...", ...}]
}
```

**Features:**
- View pending documents
- Review/approve documents via AJAX
- Submit evaluations

---

#### `GET /admin`
**Access:** Admin only (JWT + role check)  
**Purpose:** Admin dashboard

**Features:**
- Create teams
- Add students to teams
- View all evaluations
- System statistics

---

#### `POST /upload` (UNUSED)
**Status:** ⚠️ Not functional

**Issue:** Calls `upload_documents()` which doesn't exist in routes  
**Reason:** Documents upload handled by `/documents/upload` endpoint

---

#### `POST /review` (UNUSED)
**Status:** ⚠️ Not functional

**Issue:** Calls `review_documents()` which doesn't exist  
**Reason:** Document review handled by `/documents/review` endpoint

---

## 🎨 Frontend Templates

### Template Structure Overview

**Two Template Directories:**
1. `frontend/` - **ACTIVE** (Custom CSS, modern design)
2. `app/frontend/` - **LEGACY** (Bootstrap-based, outdated)

**Current Configuration:**
```python
# In app/__init__.py
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))
app = Flask(__name__, template_folder=template_dir)
```

---

### `frontend/base.html` - Base Template
**Lines of Code:** 44

**Features:**
- Purple gradient navigation bar
- Responsive container layout
- Block structure for inheritance

**Blocks:**
- `{% block title %}` - Page title
- `{% block nav_content %}` - Navigation bar content
- `{% block extra_css %}` - Additional CSS
- `{% block content %}` - Main content

**Design:**
- Purple gradient (`#667eea` → `#764ba2`)
- White cards with subtle shadows
- Clean, modern aesthetic

---

### `frontend/login.html` - Login Page
**Lines of Code:** 91

**Features:**
- Centered login card
- Purple gradient background
- Email and password fields
- Error message display

**Styling:**
- Full-screen gradient background
- Floating white card with shadow
- Smooth transitions on focus/hover
- Red error box for invalid credentials

**Form Submission:**
- Method: POST to `/login`
- Fields: `email`, `password`
- Server-side rendering for errors

---

### `frontend/dashboard_student.html` - Student Dashboard
**Lines of Code:** 212

**Sections:**

#### 1. Team Information Card
- Purple gradient card
- Shows team name and mentor
- Warning if not assigned to team

#### 2. Document Upload Section
- Dashed border upload area
- File type validation (client-side)
- AJAX upload with progress feedback
- Allowed types: PDF, PNG, JPG, JPEG, DOCX

#### 3. Document List
- Shows uploaded documents
- Color-coded status badges:
  - **Pending:** Yellow (`#ffc107`)
  - **Approved:** Green (`#28a745`)
  - **Rejected:** Red (`#dc3545`)

#### 4. Evaluation Result (if exists)
- Green gradient card
- Large marks display (X/100)
- Mentor's remarks
- Timestamp

**JavaScript Features:**
```javascript
// File upload with AJAX
fetch('/documents/upload', {
    method: 'POST',
    body: formData
})

// Display selected filename
file.addEventListener('change', function(e) {
    // Shows filename before upload
})
```

**Emojis Used:** 👋 📚 👨‍🏫 ⚠️ 📤 📁 🚀 📋 📄 ✓ 🎯 💬

---

### `frontend/dashboard_mentor.html` - Mentor Dashboard
**Lines of Code:** 253

**Sections:**

#### 1. Statistics Grid
- **Teams:** Count of assigned teams
- **Documents:** Pending review count
- **Evaluated:** Number of teams evaluated

#### 2. Document Review Table
- Columns: Team, Document, Uploaded By, Status, Action
- Review button for pending documents
- Interactive review modal (confirm/prompt)

#### 3. Evaluation Form
- Team dropdown (populated via AJAX)
- Marks input (0-100)
- Remarks textarea
- Submit button

**JavaScript Features:**
```javascript
async function loadData() {
    // Fetches teams and documents
    // Updates statistics
    // Populates table and dropdown
}

async function reviewDoc(filename) {
    // Confirm approve/reject
    // Prompt for comment
    // Submit review via AJAX
}

// Auto-load on page load
loadData();
```

**API Calls:**
- `GET /documents/mentor/docs` - Load documents
- `GET /teams/my-teams` - Load teams
- `POST /documents/review` - Submit review
- `POST /evaluations/submit` - Submit evaluation

**Emojis Used:** 👨‍🏫 📚 📄 ✅📝 🚀 📊

---

### `frontend/dashboard_admin.html` - Admin Dashboard
**Lines of Code:** 250

**Sections:**

#### 1. Statistics Grid (4 cards)
- **Users:** Total user count (placeholder)
- **Teams:** Total teams
- **Documents:** Total documents (placeholder)
- **Evaluations:** Total evaluations

#### 2. Create Team Form
- Team name input
- Mentor email input
- Submit button

#### 3. Add Student to Team Form
- Team dropdown (populated from API)
- Student email input
- Submit button

#### 4. All Evaluations Table
- Columns: Team, Mentor, Marks, Remarks, Date
- Shows all evaluations in system
- Sorted by date

**JavaScript Features:**
```javascript
async function loadData() {
    // Fetch evaluations and teams
    // Update statistics
    // Populate tables and dropdowns
}

// Create team form submission
document.getElementById('createTeamForm').addEventListener('submit', ...)

// Add student form submission
document.getElementById('addStudentForm').addEventListener('submit', ...)
```

**API Calls:**
- `GET /evaluations/all` - Load all evaluations
- `GET /teams/all` - Load all teams
- `POST /teams/create` - Create team
- `POST /teams/add-student` - Add student

**Emojis Used:** 👨‍💼 👥 📚 📄 🎯 ➕ 🚀 👨‍🎓 📊

---

### `app/frontend/` - Legacy Templates (UNUSED)

**Files:**
- `base.html` - Bootstrap-based base
- `admin_dashboard.html` - Minimal admin template
- `mentor_dashboard.html` - Minimal mentor template
- `student_dashboard.html` - Minimal student template
- `login.html` - Basic login form

**Status:** ⚠️ Not actively used (kept for reference)

**Reason for Replacement:**
- Modern custom CSS preferred over Bootstrap
- Better visual design in new templates
- More interactive features (AJAX)

---

## ⚙️ Configuration & Environment

### `.env` File
**Location:** `mini_pms/.env`

**Contents:**
```env
MONGO_URI=mongodb+srv://kush2012bhardwaj:RaidenMains05Ei21@cluster0.7fvgxjw.mongodb.net/mini_pms?retryWrites=true&w=majority
SECRET_KEY=supersecret
JWT_SECRET_KEY=jwtsecret
```

**⚠️ SECURITY ISSUES:**

1. **Hardcoded Credentials:**
   - MongoDB username: `kush2012bhardwaj`
   - MongoDB password: `RaidenMains05Ei21` (exposed)
   - Database cluster: `cluster0.7fvgxjw.mongodb.net`

2. **Weak Secrets:**
   - `SECRET_KEY=supersecret` (predictable)
   - `JWT_SECRET_KEY=jwtsecret` (predictable)

3. **Public Repository:**
   - `.env` file should be in `.gitignore`
   - Credentials should be rotated immediately

**Recommendations:**
```bash
# Generate secure secrets
python -c "import secrets; print(secrets.token_hex(32))"

# Create .env.example (template)
MONGO_URI=mongodb://localhost:27017/mini_pms
SECRET_KEY=your-secret-key-here
JWT_SECRET_KEY=your-jwt-secret-here

# Add .env to .gitignore
echo ".env" >> .gitignore
```

---

### `Dockerfile`
**Lines of Code:** 11

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "main.py"]
```

**Features:**
- Base image: Python 3.10 slim (lightweight)
- Installs dependencies from requirements.txt
- Copies entire project
- Exposes port 5000
- Runs Flask development server

**⚠️ Issues:**
1. Runs in debug mode (insecure for production)
2. No multi-stage build
3. Copies unnecessary files (venv, .git, etc.)

**Improvements:**
```dockerfile
# Add .dockerignore
venv/
*.pyc
__pycache__/
.env
.git/

# Use production server (Gunicorn)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

---

### `docker-compoee.yml` (EMPTY)
**Status:** ⚠️ File exists but is empty

**Intended Purpose:** Docker Compose configuration

**Recommended Content:**
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - MONGO_URI=mongodb://mongo:27017/mini_pms
      - SECRET_KEY=${SECRET_KEY}
      - JWT_SECRET_KEY=${JWT_SECRET_KEY}
    depends_on:
      - mongo
    volumes:
      - ./uploads:/app/uploads

  mongo:
    image: mongo:6.0
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mongo_data:
```

---

### `LICENSE`
**Type:** MIT License  
**Copyright:** 2026 Kush05Bhardwaj

**Key Points:**
- Open source
- Commercial use allowed
- Attribution required
- No warranty

---

## 💾 Database Schema

### Collections

#### 1. `users` Collection
**Purpose:** Store user accounts

```json
{
  "_id": ObjectId("..."),
  "email": "user@example.com",
  "password_hash": "$2b$12$...",
  "role": "student"
}
```

**Indexes:**
- `email` (unique) - for fast lookups

**Roles:**
- `admin` - Full system access
- `mentor` - Team management and evaluation
- `student` - Document upload and view

---

#### 2. `teams` Collection
**Purpose:** Store team information

```json
{
  "_id": ObjectId("..."),
  "name": "Team Alpha",
  "mentor_email": "mentor@example.com",
  "students": [
    "student1@example.com",
    "student2@example.com"
  ],
  "status": "active"
}
```

**Indexes:**
- `name` (unique) - team identifier
- `mentor_email` - query teams by mentor
- `students` - query team by student

---

#### 3. `documents` Collection
**Purpose:** Store document metadata

```json
{
  "_id": ObjectId("..."),
  "filename": "3f8b9c1e-4a5d-6f7e-8g9h-0i1j2k3l4m5n.pdf",
  "uploaded_by": "student@example.com",
  "team_name": "Team Alpha",
  "status": "pending",
  "uploaded_at": ISODate("2026-02-23T10:30:00Z"),
  "review_comment": null
}
```

**Indexes:**
- `filename` (unique) - document identifier
- `team_name` - query documents by team
- `status` - filter by approval status

**Status Values:**
- `pending` - Awaiting review
- `approved` - Accepted by mentor
- `rejected` - Rejected by mentor

---

#### 4. `evaluations` Collection
**Purpose:** Store team evaluations

```json
{
  "_id": ObjectId("..."),
  "team_name": "Team Alpha",
  "mentor_email": "mentor@example.com",
  "marks": 85,
  "remarks": "Excellent work on the project",
  "created_at": ISODate("2026-02-23T15:45:00Z")
}
```

**Indexes:**
- `team_name` - query evaluation by team
- `mentor_email` - query evaluations by mentor

**Note:** One evaluation per team (no constraint enforced in code)

---

### Database Relationships

```
users (email)
  ├── teams (mentor_email) - 1:N
  │   └── students[] - N:N
  ├── documents (uploaded_by) - 1:N
  └── evaluations (mentor_email) - 1:N

teams (name)
  ├── documents (team_name) - 1:N
  └── evaluations (team_name) - 1:1
```

**Missing Features:**
- No foreign key constraints (MongoDB limitation)
- No cascading deletes
- No referential integrity checks

---

## 🔌 API Endpoints Summary

### Authentication Endpoints

| Method | Endpoint | Access | Purpose |
|--------|----------|--------|---------|
| POST | `/auth/register` | Public | Create user account |
| POST | `/auth/login` | Public | Get JWT token |

### Team Management Endpoints

| Method | Endpoint | Access | Purpose |
|--------|----------|--------|---------|
| POST | `/teams/create` | Admin | Create new team |
| POST | `/teams/add-student` | Admin | Add student to team |
| GET | `/teams/my-team` | Student | Get student's team |
| GET | `/teams/my-teams` | Mentor | Get mentor's teams |
| GET | `/teams/all` | Admin | Get all teams |

### Document Endpoints

| Method | Endpoint | Access | Purpose |
|--------|----------|--------|---------|
| POST | `/documents/upload` | Student | Upload document |
| GET | `/documents/mentor/docs` | Mentor | Get team documents |
| POST | `/documents/review` | Mentor | Approve/reject document |

### Evaluation Endpoints

| Method | Endpoint | Access | Purpose |
|--------|----------|--------|---------|
| POST | `/evaluations/submit` | Mentor | Submit team evaluation |
| GET | `/evaluations/my-result` | Student | Get team result |
| GET | `/evaluations/all` | Admin | Get all evaluations |

### UI Endpoints

| Method | Endpoint | Access | Purpose |
|--------|----------|--------|---------|
| GET | `/` | Public | Redirect to login |
| GET/POST | `/login` | Public | Login page |
| GET | `/student` | Student | Student dashboard |
| GET | `/mentor` | Mentor | Mentor dashboard |
| GET | `/admin` | Admin | Admin dashboard |

---

## 🔒 Security Features

### Implemented Security

1. **Password Hashing:**
   - Werkzeug's `generate_password_hash()` (PBKDF2)
   - Passwords never stored in plaintext

2. **JWT Authentication:**
   - Token-based authentication
   - Role claims for authorization
   - Cookie and header support

3. **Role-Based Access Control:**
   - `@role_required()` decorator
   - Endpoint-level protection
   - 403 responses for unauthorized access

4. **File Upload Security:**
   - Extension whitelist
   - Size limit (5 MB)
   - UUID filenames (prevents path traversal)
   - Team-specific folders

5. **Input Validation:**
   - Password length requirement (≥6 chars)
   - Role validation (Admin/Mentor/Student)
   - File type validation

### Security Issues

⚠️ **Critical Issues:**

1. **Exposed Credentials:**
   - MongoDB password in `.env` file
   - Weak secret keys
   - `.env` not in `.gitignore`

2. **Debug Mode in Production:**
   - `debug=True` in `main.py`
   - Stack traces exposed to users

3. **No HTTPS Enforcement:**
   - `JWT_COOKIE_SECURE = False`
   - Tokens transmitted over HTTP

4. **No CSRF Protection:**
   - `JWT_COOKIE_CSRF_PROTECT = False`
   - Vulnerable to CSRF attacks

5. **Missing Input Validation:**
   - No marks range validation (0-100)
   - No email format validation
   - No file content validation (only extension)

6. **Missing Authorization Checks:**
   - Document review doesn't verify mentor ownership
   - Students can upload to teams they don't belong to
   - No deletion endpoints with proper authorization

7. **No Rate Limiting:**
   - Vulnerable to brute force attacks
   - No login attempt throttling

8. **No CORS Configuration:**
   - Accepts requests from any origin

### Recommended Fixes

```python
# 1. Secure configuration
JWT_COOKIE_SECURE = True  # HTTPS only
JWT_COOKIE_CSRF_PROTECT = True
DEBUG = False

# 2. Add rate limiting
from flask_limiter import Limiter
limiter = Limiter(app, key_func=get_remote_address)

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    ...

# 3. Add input validation
from email_validator import validate_email

def validate_marks(marks):
    if not (0 <= marks <= 100):
        raise ValueError("Marks must be between 0 and 100")

# 4. Add CORS
from flask_cors import CORS
CORS(app, origins=["https://yourdomain.com"])

# 5. Add file content validation
import magic
mime = magic.Magic(mime=True)
file_type = mime.from_buffer(file.read(1024))
if file_type not in ALLOWED_MIME_TYPES:
    raise ValueError("Invalid file content")
```

---

## 🚀 Deployment Files

### Current Deployment Setup

**Method:** Docker containerization  
**Server:** Flask development server (⚠️ Not production-ready)  
**Database:** MongoDB Atlas (cloud)

### Production Deployment Recommendations

#### 1. Use Production WSGI Server

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 main:app
```

#### 2. Environment Variables

```bash
# Production .env
export MONGO_URI="mongodb+srv://..."
export SECRET_KEY="$(openssl rand -hex 32)"
export JWT_SECRET_KEY="$(openssl rand -hex 32)"
export FLASK_ENV="production"
```

#### 3. Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /uploads {
        alias /path/to/uploads;
    }
}
```

#### 4. SSL/TLS Certificate

```bash
# Using Certbot
sudo certbot --nginx -d yourdomain.com
```

#### 5. Docker Production Setup

```dockerfile
# Multi-stage build
FROM python:3.10-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

FROM python:3.10-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
```

---

## ⚠️ Issues & Recommendations

### Critical Issues

| Priority | Issue | Impact | Fix |
|----------|-------|--------|-----|
| 🔴 HIGH | Exposed credentials in `.env` | Security breach | Rotate credentials, add to `.gitignore` |
| 🔴 HIGH | Debug mode enabled | Information disclosure | Set `DEBUG=False` |
| 🔴 HIGH | No HTTPS enforcement | Man-in-the-middle attacks | Enable `JWT_COOKIE_SECURE=True`, use HTTPS |
| 🔴 HIGH | Missing authorization checks | Privilege escalation | Verify ownership before operations |
| 🟡 MEDIUM | No input validation | Data integrity issues | Add validation for all inputs |
| 🟡 MEDIUM | No rate limiting | Brute force attacks | Implement Flask-Limiter |
| 🟡 MEDIUM | Production server not used | Performance issues | Use Gunicorn/uWSGI |

### Code Quality Issues

1. **Unused Files:**
   - `app/auth/ui_protect.py` - Not referenced
   - `app/frontend/` templates - Replaced by `frontend/`
   - `app/ui/routes.py` - Functions `upload_ui()` and `review_ui()` broken

2. **Incomplete Features:**
   - Local cache has no TTL implementation
   - Email service only prints to console
   - Docker Compose file is empty
   - `docker-compoee.yml` has typo in filename

3. **Missing Features:**
   - No user deletion
   - No team deletion
   - No document deletion
   - No password reset
   - No email verification
   - No user profile management
   - No search functionality
   - No pagination controls in UI

4. **Database Issues:**
   - No indexes defined
   - No data migration strategy
   - No backup mechanism
   - Multiple evaluations per team possible (no constraint)

### Code Improvements

#### 1. Add .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
ENV/
env/

# Environment
.env
.env.local

# Uploads
uploads/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
```

#### 2. Add Database Indexes

```python
# In app/db.py
def setup_indexes():
    db = get_db()
    db.users.create_index("email", unique=True)
    db.teams.create_index("name", unique=True)
    db.teams.create_index("mentor_email")
    db.teams.create_index("students")
    db.documents.create_index("filename", unique=True)
    db.documents.create_index("team_name")
    db.evaluations.create_index("team_name", unique=True)
```

#### 3. Add Input Validation

```python
# app/validators.py
from email_validator import validate_email, EmailNotValidError

def validate_user_input(email, password, role):
    try:
        validate_email(email)
    except EmailNotValidError:
        raise ValueError("Invalid email format")
    
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")
    
    if role not in ['Admin', 'Mentor', 'Student']:
        raise ValueError("Invalid role")
    
    return True
```

#### 4. Add Error Logging

```python
# In app/__init__.py
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/mini_pms.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Mini PMS startup')
```

#### 5. Add API Documentation

```python
# Use Flask-RESTX or similar
from flask_restx import Api, Resource

api = Api(app, version='1.0', title='Mini PMS API',
    description='Project Management System API')

@api.route('/auth/register')
class Register(Resource):
    @api.doc(description='Register a new user')
    @api.expect(user_model)
    def post(self):
        ...
```

### Testing Recommendations

```python
# tests/test_auth.py
import unittest
from app import create_app
from app.db import get_db

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True
    
    def test_register(self):
        response = self.client.post('/auth/register', json={
            'email': 'test@example.com',
            'password': 'password123',
            'role': 'Student'
        })
        self.assertEqual(response.status_code, 201)
    
    def test_login(self):
        # Register first
        self.client.post('/auth/register', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        # Then login
        response = self.client.post('/auth/login', json={
            'email': 'test@example.com',
            'password': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
```

---

## 📊 Code Statistics

### Lines of Code by Module

| Module | Files | Total Lines | Code Lines |
|--------|-------|-------------|------------|
| Core (`app/`) | 6 | ~80 | ~60 |
| Auth | 4 | ~78 | ~65 |
| Teams | 2 | ~78 | ~72 |
| Documents | 2 | ~113 | ~105 |
| Evaluations | 2 | ~59 | ~51 |
| UI Routes | 1 | ~95 | ~85 |
| Templates (active) | 5 | ~850 | ~750 |
| **Total** | **22** | **~1,353** | **~1,188** |

### Technology Distribution

- **Python:** ~500 lines (42%)
- **HTML/Jinja2:** ~750 lines (63%)
- **JavaScript:** ~350 lines (29%)
- **CSS:** ~300 lines (25%)

*(Percentages don't add to 100% as HTML files contain multiple languages)*

---

## 🎓 Learning Resources

### For Future Development

1. **Flask Best Practices:**
   - [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
   - [Flask Documentation](https://flask.palletsprojects.com/)

2. **MongoDB:**
   - [MongoDB University](https://university.mongodb.com/)
   - [PyMongo Documentation](https://pymongo.readthedocs.io/)

3. **Security:**
   - [OWASP Top 10](https://owasp.org/www-project-top-ten/)
   - [Flask Security Checklist](https://flask.palletsprojects.com/en/2.3.x/security/)

4. **Testing:**
   - [Python Testing with pytest](https://docs.pytest.org/)
   - [Flask Testing](https://flask.palletsprojects.com/en/2.3.x/testing/)

---

## 📝 Conclusion

**Mini PMS** is a functional role-based project management system with a clean architecture and modern UI. However, several security and production-readiness issues need to be addressed before deployment.

### Strengths
✅ Clear separation of concerns (modular structure)  
✅ Role-based access control  
✅ Modern, responsive UI  
✅ RESTful API design  
✅ Docker support  

### Weaknesses
❌ Security vulnerabilities (exposed credentials, no HTTPS)  
❌ Missing production server setup  
❌ Incomplete error handling  
❌ No automated tests  
❌ Limited input validation  

### Next Steps
1. **Immediate:** Rotate credentials, add `.env` to `.gitignore`
2. **Short-term:** Add input validation, rate limiting, HTTPS
3. **Medium-term:** Write tests, add logging, use production server
4. **Long-term:** Add features (user management, search, analytics)

---

**Generated:** February 23, 2026  
**By:** GitHub Copilot  
**For:** Kushagra Bhardwaj (@Kush05Bhardwaj)
