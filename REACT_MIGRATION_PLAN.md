# 🚀 React Frontend Migration Plan

## Overview
Transition from Jinja2 HTML templates to a modern React.js frontend with separate backend API.

---

## 🎯 Architecture

### Current Stack
- **Frontend:** Jinja2 templates (server-side rendering)
- **Backend:** Flask (serves both API and HTML)
- **Communication:** Form submissions, page reloads

### New Stack
- **Frontend:** React.js (SPA - Single Page Application)
- **Backend:** Flask (REST API only)
- **Communication:** AJAX/Fetch API with JWT tokens
- **Build Tool:** Vite (fast, modern)
- **Styling:** TailwindCSS or Material-UI
- **State Management:** React Context API / React Query

---

## 📁 New Project Structure

```
Project-Management-System/
├── mini_pms/                    # Backend (Flask API)
│   ├── app/
│   │   ├── auth/
│   │   ├── teams/
│   │   ├── documents/
│   │   ├── evaluations/
│   │   └── ui/                  # ❌ DELETE - No longer needed
│   ├── frontend/                # ❌ DELETE - Old templates
│   ├── main.py
│   └── requirements.txt
│
└── frontend/                    # ✨ NEW React App
    ├── public/
    ├── src/
    │   ├── components/
    │   │   ├── Navbar.jsx
    │   │   ├── ProtectedRoute.jsx
    │   │   └── ...
    │   ├── pages/
    │   │   ├── Login.jsx
    │   │   ├── StudentDashboard.jsx
    │   │   ├── MentorDashboard.jsx
    │   │   └── AdminDashboard.jsx
    │   ├── services/
    │   │   ├── api.js
    │   │   └── auth.js
    │   ├── context/
    │   │   └── AuthContext.jsx
    │   ├── utils/
    │   │   └── constants.js
    │   ├── App.jsx
    │   └── main.jsx
    ├── package.json
    └── vite.config.js
```

---

## 🛠️ Implementation Steps

### Phase 1: Backend Preparation ✅
- [x] Remove UI blueprint from Flask app
- [x] Update CORS configuration
- [x] Ensure all endpoints return JSON
- [x] Test API endpoints independently

### Phase 2: React Setup
- [ ] Create React app with Vite
- [ ] Install dependencies (React Router, Axios, TailwindCSS)
- [ ] Configure API proxy
- [ ] Set up authentication context

### Phase 3: Core Components
- [ ] Create authentication service
- [ ] Build login page
- [ ] Implement protected routes
- [ ] Create navigation component

### Phase 4: Dashboard Pages
- [ ] Student Dashboard
  - [ ] Team information card
  - [ ] Document upload form
  - [ ] Document list with status
  - [ ] Evaluation results display
  
- [ ] Mentor Dashboard
  - [ ] Statistics cards
  - [ ] Document review table
  - [ ] Evaluation submission form
  
- [ ] Admin Dashboard
  - [ ] Team creation form
  - [ ] Student assignment form
  - [ ] All evaluations table
  - [ ] System statistics

### Phase 5: Enhancement Features
- [ ] Real-time notifications
- [ ] File preview
- [ ] Advanced search/filtering
- [ ] Dark mode
- [ ] Responsive design
- [ ] Loading states & error handling

### Phase 6: Deployment
- [ ] Build production React app
- [ ] Configure Nginx to serve React + Flask API
- [ ] Set up environment variables
- [ ] Deploy to production

---

## 🔧 Backend Changes Required

### 1. Remove UI Blueprint
```python
# app/__init__.py
# REMOVE:
from .ui.routes import ui_bp
app.register_blueprint(ui_bp)
```

### 2. Add CORS Support
```python
# requirements.txt
flask-cors==4.0.0

# app/__init__.py
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, 
         origins=["http://localhost:5173"],  # Vite dev server
         supports_credentials=True)
    ...
```

### 3. Update JWT Configuration
```python
# app/config.py
JWT_TOKEN_LOCATION = ['headers']  # Remove cookies, use headers only
JWT_HEADER_NAME = 'Authorization'
JWT_HEADER_TYPE = 'Bearer'
```

### 4. Delete Old Templates
```bash
# Remove frontend/ directory (old HTML templates)
# Remove app/frontend/ directory (legacy templates)
# Remove app/ui/ directory (UI routes)
```

---

## 📦 React Dependencies

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "axios": "^1.6.0",
    "react-query": "^3.39.3",
    "zustand": "^4.4.7",
    "@headlessui/react": "^1.7.17",
    "@heroicons/react": "^2.1.1"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0",
    "tailwindcss": "^3.3.0",
    "autoprefixer": "^10.4.16",
    "postcss": "^8.4.32"
  }
}
```

---

## 🎨 UI/UX Improvements

### Design System
- **Colors:** Keep purple gradient theme (#667eea → #764ba2)
- **Font:** Inter or Poppins
- **Components:** Consistent spacing, shadows, transitions
- **Icons:** Heroicons or Lucide React

### Responsive Breakpoints
```js
// tailwind.config.js
module.exports = {
  theme: {
    screens: {
      'sm': '640px',
      'md': '768px',
      'lg': '1024px',
      'xl': '1280px',
      '2xl': '1536px',
    }
  }
}
```

### Features to Add
1. **Toast Notifications** - React Hot Toast
2. **Loading Spinners** - Custom animated components
3. **File Upload Progress** - Visual progress bars
4. **Data Tables** - Sorting, filtering, pagination
5. **Form Validation** - React Hook Form + Zod
6. **Dark Mode** - System preference detection

---

## 🔐 Authentication Flow

```javascript
// services/auth.js
class AuthService {
  async login(email, password) {
    const response = await api.post('/auth/login', { email, password });
    const { access_token } = response.data;
    localStorage.setItem('token', access_token);
    return this.decodeToken(access_token);
  }

  async logout() {
    localStorage.removeItem('token');
    window.location.href = '/login';
  }

  getToken() {
    return localStorage.getItem('token');
  }

  isAuthenticated() {
    const token = this.getToken();
    if (!token) return false;
    // Check if token is expired
    return !this.isTokenExpired(token);
  }

  getRole() {
    const token = this.getToken();
    if (!token) return null;
    const decoded = this.decodeToken(token);
    return decoded.role;
  }
}
```

---

## 📡 API Service

```javascript
// services/api.js
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor - Add JWT token
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor - Handle 401 errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

export default api;
```

---

## 🚀 Deployment Strategy

### Development
```bash
# Terminal 1 - Backend
cd mini_pms
python main.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

### Production Build
```bash
# Build React app
cd frontend
npm run build

# Serve with Flask
cd ../mini_pms
# Configure Flask to serve React build files
```

### Nginx Configuration
```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # React frontend
    location / {
        root /path/to/frontend/dist;
        try_files $uri /index.html;
    }

    # Flask API
    location /api {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Uploads
    location /uploads {
        alias /path/to/mini_pms/uploads;
    }
}
```

---

## ⚡ Performance Optimizations

1. **Code Splitting** - React.lazy() for route-based splitting
2. **Memoization** - useMemo, useCallback for expensive operations
3. **Virtual Scrolling** - For large document/evaluation lists
4. **Image Optimization** - WebP format, lazy loading
5. **API Caching** - React Query with staleTime configuration
6. **Bundle Size** - Tree shaking, dynamic imports

---

## 🧪 Testing Strategy

### Frontend Testing
```bash
npm install --save-dev vitest @testing-library/react @testing-library/jest-dom
```

- **Unit Tests:** Components, utilities, services
- **Integration Tests:** User flows, API integration
- **E2E Tests:** Cypress or Playwright

### Backend Testing (Existing)
- API endpoint tests
- Authentication tests
- Authorization tests

---

## 📝 Migration Checklist

### Backend Cleanup
- [ ] Remove `app/ui/routes.py`
- [ ] Remove `frontend/` templates directory
- [ ] Remove `app/frontend/` legacy templates
- [ ] Add `flask-cors` to requirements.txt
- [ ] Update `app/__init__.py` to enable CORS
- [ ] Update JWT configuration for headers-only

### Frontend Setup
- [ ] Initialize Vite + React app
- [ ] Install dependencies
- [ ] Configure Tailwind CSS
- [ ] Set up React Router
- [ ] Create folder structure

### Feature Implementation
- [ ] Authentication (Login/Logout)
- [ ] Student Dashboard
- [ ] Mentor Dashboard
- [ ] Admin Dashboard
- [ ] File Upload Component
- [ ] Document Review Interface
- [ ] Evaluation Forms
- [ ] Error Handling
- [ ] Loading States

### Polish & Deploy
- [ ] Responsive design
- [ ] Accessibility (a11y)
- [ ] Error boundaries
- [ ] Production build
- [ ] Deployment configuration

---

## 💡 Additional Enhancements

### Potential New Features
1. **Real-time Updates** - WebSocket for live notifications
2. **File Preview** - PDF viewer, image lightbox
3. **Comments System** - Threaded comments on documents
4. **Analytics Dashboard** - Charts for admin (Chart.js/Recharts)
5. **Email Notifications** - Integrate with backend email service
6. **Multi-language Support** - i18n
7. **PWA Support** - Offline functionality
8. **Export Features** - PDF reports, CSV downloads

---

## 🔗 Useful Resources

- [Vite Documentation](https://vitejs.dev/)
- [React Router v6](https://reactrouter.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [React Query](https://tanstack.com/query/latest)
- [Axios](https://axios-http.com/)
- [Headless UI](https://headlessui.com/)

---

**Next Action:** Run the setup script to create the React frontend!
