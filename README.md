# 🚀 Mini Project Management System (Mini PMS)

A role-based Project Management System built with Flask, MongoDB, and modern web technologies for seamless collaboration between students, mentors, and administrators.

---

## ✨ Features

- **JWT Authentication** - Secure token-based auth with cookie support
- **Role-Based Access** - Student, Mentor, Admin roles with specific permissions
- **Document Management** - Upload, review, approve/reject documents with team-specific folders
- **Evaluation System** - Mentors submit marks and remarks for teams
- **Modern UI** - Responsive dashboards with AJAX interactions and real-time feedback

**User Capabilities:**
- **Students:** Upload documents, track approval status, view evaluations
- **Mentors:** Review documents, submit evaluations, manage multiple teams
- **Admins:** Create teams, assign users, view all evaluations

---

## 🛠️ Tech Stack

**Backend:** Flask 3.1.2 • MongoDB (pymongo) • Flask-JWT-Extended • Bcrypt  
**Frontend:** Jinja2 • JavaScript (ES6+) • CSS3  
**DevOps:** Docker • Python 3.10

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ • MongoDB • Git

### Installation
```bash
# Clone repository
git clone https://github.com/Kush05Bhardwaj/Project-Management-System.git
cd Project-Management-System/mini_pms

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

**Access:** http://localhost:5000

### Docker Deployment
```bash
docker build -t mini-pms .
docker run -p 5000:5000 mini-pms
```

---

## 📡 API Endpoints

### Authentication
```http
POST /auth/register          # Register user (email, password, role)
POST /auth/login             # Login and get JWT token
```

### Teams
```http
POST /teams/create           # Create team (Admin)
POST /teams/add-student      # Add student to team (Admin)
GET  /teams/my-team          # Get student's team
GET  /teams/my-teams         # Get mentor's teams
GET  /teams/all              # Get all teams (Admin)
```

### Documents
```http
POST /documents/upload       # Upload document (Student)
GET  /documents/team/<name>  # Get team documents
POST /documents/review/<id>  # Approve/reject document (Mentor)
```

### Evaluations
```http
POST /evaluations/submit     # Submit evaluation (Mentor)
GET  /evaluations/team/<name> # Get team evaluation
GET  /evaluations/all        # Get all evaluations (Admin)
```

**Authentication:** Include `Authorization: Bearer <jwt_token>` header for protected routes.

---

## 🌐 Web Routes

| Route | Access | Description |
|-------|--------|-------------|
| `/` | Public | Login page |
| `/dashboard` | Authenticated | Role-based redirect |
| `/student` | Student | Document upload & evaluation view |
| `/mentor` | Mentor | Document review & evaluation submission |
| `/admin` | Admin | Team management & system overview |

---

## 📁 Project Structure

```
mini_pms/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration
│   ├── db.py                # MongoDB connection
│   ├── auth/                # Authentication (models, routes, utils)
│   ├── teams/               # Team management
│   ├── documents/           # Document upload/review
│   ├── evaluations/         # Evaluation system
│   └── ui/                  # Web UI routes
├── frontend/                # HTML templates
├── uploads/                 # File storage
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
└── DOCKERFILE               # Container config
```

---

## 🔒 Security

- ✅ Bcrypt password hashing
- ✅ JWT authentication with CSRF protection
- ✅ Role-based access control
- ✅ File validation & UUID filenames
- ✅ Protected API routes

---

## 🧪 Quick Test

```bash
# Create admin
curl -X POST http://localhost:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@test.com","password":"admin123","role":"admin"}'

# Login
curl -X POST http://localhost:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@test.com","password":"admin123"}'

# Create team (use token from login)
curl -X POST http://localhost:5000/teams/create \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <token>" \
  -d '{"name":"Team Alpha","mentor_email":"mentor@test.com"}'
```

---

## 📊 Database Schema

**Collections:** `users` • `teams` • `documents` • `evaluations`

```json
// User
{"email": "user@example.com", "password_hash": "...", "role": "student"}

// Team
{"name": "Team Alpha", "mentor_email": "...", "students": [...]}

// Document
{"team_name": "...", "filename": "...", "status": "pending", "uploaded_by": "..."}

// Evaluation
{"team_name": "...", "mentor_email": "...", "marks": 85, "remarks": "..."}
```

---

## 💡 Configuration

Edit `app/config.py` or use `.env`:
```env
MONGO_URI=mongodb://localhost:27017/
JWT_SECRET_KEY=your-secret-key-here
UPLOAD_FOLDER=uploads/
```

---

## 🐛 Troubleshooting

**MongoDB Error:** Ensure MongoDB is running - `mongod --version`  
**Port Conflict:** Change port in `main.py` - `app.run(port=5001)`  
**Docker Issues:** Rebuild with `docker build --no-cache -t mini-pms .`  
**JWT Issues:** Clear browser cookies or regenerate secret key

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature/name`
5. Open Pull Request

---

## 👨‍💻 Author

**Kushagra Bhardwaj**  
GitHub: [@Kush05Bhardwaj](https://github.com/Kush05Bhardwaj)  
Repository: [Project-Management-System](https://github.com/Kush05Bhardwaj/Project-Management-System)

---

## 📝 License

MIT License - Open source and free to use.

