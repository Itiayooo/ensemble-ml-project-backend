from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/api/assessment", tags=["Assessment"])


@router.post("/user", response_model=schemas.UserResponse)
def create_or_get_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user or return existing one.
    Frontend calls this first before starting assessment.
    """
    db_user = crud.create_user(db, user)
    return db_user


@router.post("/start", response_model=schemas.SessionStatusResponse)
def start_assessment(request: schemas.SessionStartRequest, db: Session = Depends(get_db)):
    """
    Create a new assessment session.
    Randomly assigns questions/problems to the session.
    """
    # Verify user exists
    user = crud.get_user_by_id(db, request.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get random question/problem IDs to assign
    quiz_questions = crud.get_random_quiz_questions(db, count=20)
    coding_problems = crud.get_random_coding_problems(db, count=5)
    audit_problems = crud.get_random_audit_problems(db, count=5)

    quiz_ids = [q.id for q in quiz_questions]
    coding_ids = [p.id for p in coding_problems]
    audit_ids = [p.id for p in audit_problems]

    # Create session
    session = crud.create_session(db, request.user_id, quiz_ids, coding_ids, audit_ids)

    return {
        "session_id": session.id,
        "quiz_completed": False,
        "coding_completed": False,
        "audit_completed": False,
        "status": "in_progress"
    }


@router.get("/status/{session_id}", response_model=schemas.SessionStatusResponse)
def get_session_status(session_id: int, db: Session = Depends(get_db)):
    """
    Check current session status.
    Frontend uses this to know which stages are unlocked.
    """
    session = crud.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    return {
        "session_id": session.id,
        "quiz_completed": session.quiz_completed,
        "coding_completed": session.coding_completed,
        "audit_completed": session.audit_completed,
        "status": session.status
    }