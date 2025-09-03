# 🎓 AI EdTech Student Management API

Day 1 Project: Production-ready FastAPI application for student management.

## 🚀 Features

- ✅ CRUD operations for students
- ✅ Input validation with Pydantic
- ✅ Search functionality
- ✅ Pagination support
- ✅ Proper error handling
- ✅ API documentation
- ✅ Health monitoring
- ✅ CORS support
- ✅ Logging

## 📁 Project Structure

```
day1_student_api/
├── app/
│   ├── main.py              # FastAPI application
│   ├── models/
│   │   └── student.py       # Pydantic models
│   ├── routes/
│   │   └── students.py      # API endpoints
│   └── services/
│       └── student_service.py # Business logic
├── requirements.txt
└── README.md
```

## 🛠️ Setup Instructions

1. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the application:**
```bash
uvicorn app.main:app --reload
```

4. **Access the API:**
- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc
- Health Check: http://localhost:8000/health

## 📚 API Endpoints

### Students Management
- `POST /api/v1/students/` - Create new student
- `GET /api/v1/students/` - Get all students (with pagination & search)
- `GET /api/v1/students/{id}` - Get student by ID
- `PUT /api/v1/students/{id}` - Update student
- `DELETE /api/v1/students/{id}` - Delete student

### System
- `GET /` - Welcome message
- `GET /health` - Health check

## 🧪 Testing Examples

### Create Student
```bash
curl -X POST "http://localhost:8000/api/v1/students/" \
-H "Content-Type: application/json" \
-d '{
  "name": "Vicky Sharma",
  "email": "vicky@example.com",
  "age": 21,
  "grade": "college",
  "subjects": ["Python", "AI", "Machine Learning"]
}'
```

### Get All Students
```bash
curl "http://localhost:8000/api/v1/students/?limit=5&skip=0&search=vicky"
```

### Get Student by ID
```bash
curl "http://localhost:8000/api/v1/students/1"
```

## 🎯 Production Features Implemented

1. **Clean Architecture** - Separation of concerns
2. **Input Validation** - Pydantic models with constraints
3. **Error Handling** - Custom exceptions and global handler
4. **API Documentation** - Auto-generated with FastAPI
5. **Health Monitoring** - Health check endpoint
6. **CORS Support** - For frontend integration
7. **Logging** - Structured logging for debugging
8. **Type Hints** - Full type safety

## 🚀 Next Steps (Day 2)

- Database integration (SQLAlchemy)
- Authentication system
- Unit testing
- Environment configuration
- Docker containerization

---

**Built with ❤️ for AI EdTech Startup**