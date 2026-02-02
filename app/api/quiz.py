from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas

router = APIRouter(prefix="/api/quiz", tags=["Quiz"])


@router.get("/start/{session_id}", response_model=schemas.QuizStartResponse)
def start_quiz(session_id: int, db: Session = Depends(get_db)):
    """
    Fetch 10 random quiz questions for the user.
    Does NOT include correct answers (security).
    """
    # Verify session exists
    session = crud.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    # Check if quiz already completed
    if session.quiz_completed:
        raise HTTPException(status_code=400, detail="Quiz already completed")

    # Get random questions
    questions = crud.get_random_quiz_questions(db, count=10)

    if not questions:
        raise HTTPException(status_code=500, detail="No quiz questions in database. Run the seed script first.")

    return {
        "session_id": session_id,
        "questions": questions,
        "total_questions": len(questions)
    }


@router.post("/submit", response_model=schemas.QuizSubmitResponse)
def submit_quiz(submission: schemas.QuizSubmission, db: Session = Depends(get_db)):
    """
    Submit quiz answers.
    Backend validates each answer and calculates score.
    """
    # Verify session
    session = crud.get_session_by_id(db, submission.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if session.quiz_completed:
        raise HTTPException(status_code=400, detail="Quiz already completed")

    # Validate and save answers
    results = crud.save_quiz_responses(db, submission.session_id, submission.answers)

    # Calculate score
    correct = sum(1 for r in results if r["is_correct"])
    total = len(results)
    score = (correct / total) * 100 if total > 0 else 0

    # Mark quiz as completed
    crud.update_session_stage(db, submission.session_id, "quiz")

    return {
        "score": round(score, 2),
        "correct": correct,
        "total": total,
        "results": results,
        "passed": score >= 50
    }