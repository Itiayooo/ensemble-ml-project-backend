from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api import quiz, coding, audit, assessment
from dotenv import load_dotenv
import os

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title="SkillAssess Pro API",
    description="Backend for Ensemble ML-based Entry-Level Skill Assessment",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:5173")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routers
app.include_router(assessment.router)
app.include_router(quiz.router)
app.include_router(coding.router)
app.include_router(audit.router)

@app.get("/")
def read_root():
    return {
        "message": "SkillAssess Pro API is running",
        "version": "1.0.0",
        "status": "active",
        "endpoints": {
            "docs": "/docs",
            "assessment": "/api/assessment",
            "quiz": "/api/quiz",
            "coding": "/api/coding",
            "audit": "/api/audit"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}