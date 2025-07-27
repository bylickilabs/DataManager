# 🧩 Universal Data Manager – Fullstack Project

A complete system for working with MySQL, PostgreSQL, and MongoDB in parallel – consisting of:

## 📦 Backend (FastAPI)
- REST API for SQL and MongoDB queries
- CORS support for frontend integration
- Separate sessions per database
- Entry file: `backend/main.py`

## 🎨 Frontend (React + Tailwind)
- Dashboard for executing and visualizing queries
- Supports SQL and MongoDB querying
- Main component: `frontend/src/Dashboard.tsx`

## 🧪 Usage

```bash
# Backend
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

---

Created by BYLICKILABS – 2025
