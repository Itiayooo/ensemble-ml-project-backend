from sqlalchemy.orm import Session
from sqlalchemy import func
from app import models, schemas
from datetime import datetime


# ==================== QUIZ CRUD ====================

def seed_quiz_question(db: Session, question: schemas.QuizQuestionCreate):
    """Add a single question to the database"""
    db_question = models.QuizQuestion(
        question=question.question,
        options=question.options,
        correct_answer=question.correct_answer,
        difficulty=question.difficulty,
        category=question.category
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_quiz_question_count(db: Session) -> int:
    """Check how many questions exist"""
    return db.query(models.QuizQuestion).count()

def get_random_quiz_questions(db: Session, count: int = 10) -> list:
    """Fetch N random questions from database"""
    return (
        db.query(models.QuizQuestion)
        .order_by(func.random())
        .limit(count)
        .all()
    )

def get_quiz_question_by_id(db: Session, question_id: int):
    """Fetch a single question by ID"""
    return db.query(models.QuizQuestion).filter(models.QuizQuestion.id == question_id).first()

def save_quiz_responses(db: Session, session_id: int, answers: list) -> list:
    """
    Save all quiz answers AND validate them.
    Returns list of results with is_correct flag.
    """
    results = []
    for answer in answers:
        question = get_quiz_question_by_id(db, answer.question_id)
        if not question:
            continue

        is_correct = (question.correct_answer == answer.selected_answer)

        db_response = models.QuizResponse(
            session_id=session_id,
            question_id=answer.question_id,
            selected_answer=answer.selected_answer,
            is_correct=is_correct,
            time_spent=answer.time_spent
        )
        db.add(db_response)

        results.append({
            "question_id": answer.question_id,
            "is_correct": is_correct,
            "time_spent": answer.time_spent
        })

    db.commit()
    return results


# ==================== CODING CRUD ====================

def seed_coding_problem(db: Session, problem: schemas.CodingProblemCreate):
    """Add a single coding problem to the database"""
    db_problem = models.CodingProblem(
        title=problem.title,
        description=problem.description,
        difficulty=problem.difficulty,
        starter_code_python=problem.starter_code_python,
        starter_code_javascript=problem.starter_code_javascript,
        starter_code_java=problem.starter_code_java,
        test_cases=problem.test_cases,
        constraints=problem.constraints,
        examples=problem.examples
    )
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_coding_problem_count(db: Session) -> int:
    return db.query(models.CodingProblem).count()

def get_random_coding_problems(db: Session, count: int = 5) -> list:
    """Fetch N random coding problems"""
    return (
        db.query(models.CodingProblem)
        .order_by(func.random())
        .limit(count)
        .all()
    )

def get_coding_problem_by_id(db: Session, problem_id: int):
    return db.query(models.CodingProblem).filter(models.CodingProblem.id == problem_id).first()

def save_coding_submission(db: Session, submission: schemas.CodingSubmission, test_results: dict, code_metrics: dict):
    """Save coding submission with test results and code metrics"""
    db_submission = models.CodingSubmission(
        session_id=submission.session_id,
        problem_id=submission.problem_id,
        language=submission.language,
        code=submission.code,
        run_count=submission.run_count,
        keystrokes=submission.keystrokes,
        total_time=submission.total_time,
        edit_events=submission.edit_events,
        tests_passed=test_results["passed"],
        tests_total=test_results["total"],
        lines_of_code=code_metrics.get("lines_of_code"),
        cyclomatic_complexity=code_metrics.get("cyclomatic_complexity"),
        halstead_metrics=code_metrics.get("halstead_metrics")
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission


# ==================== AUDIT CRUD ====================

def seed_audit_problem(db: Session, problem: schemas.AuditProblemCreate):
    """Add a single audit problem to the database"""
    db_problem = models.AuditProblem(
        title=problem.title,
        description=problem.description,
        difficulty=problem.difficulty,
        buggy_code_python=problem.buggy_code_python,
        buggy_code_javascript=problem.buggy_code_javascript,
        known_issues=problem.known_issues,
        test_cases=problem.test_cases
    )
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem

def get_audit_problem_count(db: Session) -> int:
    return db.query(models.AuditProblem).count()

def get_random_audit_problems(db: Session, count: int = 5) -> list:
    """Fetch N random audit problems"""
    return (
        db.query(models.AuditProblem)
        .order_by(func.random())
        .limit(count)
        .all()
    )

def get_audit_problem_by_id(db: Session, problem_id: int):
    return db.query(models.AuditProblem).filter(models.AuditProblem.id == problem_id).first()

def save_audit_submission(db: Session, submission: schemas.AuditSubmission, audit_results: dict):
    """Save audit submission with results"""
    db_submission = models.AuditSubmission(
        session_id=submission.session_id,
        problem_id=submission.problem_id,
        language=submission.language,
        original_code=audit_results["original_code"],
        modified_code=submission.modified_code,
        edit_count=submission.edit_count,
        lines_changed=submission.lines_changed,
        edit_history=submission.edit_history,
        total_time=submission.total_time,
        bugs_fixed=audit_results["bugs_fixed"],
        bugs_total=audit_results["bugs_total"],
        tests_passed=audit_results["tests_passed"]
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission


# ==================== SESSION CRUD ====================

def create_user(db: Session, user: schemas.UserCreate):
    """Create a new user or return existing"""
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        return existing

    db_user = models.User(email=user.email, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_session(db: Session, user_id: int, quiz_ids: list, coding_ids: list, audit_ids: list):
    """Create a new assessment session with assigned questions"""
    db_session = models.AssessmentSession(
        user_id=user_id,
        assigned_quiz_questions=quiz_ids,
        assigned_coding_problems=coding_ids,
        assigned_audit_problems=audit_ids
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

def get_session_by_id(db: Session, session_id: int):
    return db.query(models.AssessmentSession).filter(models.AssessmentSession.id == session_id).first()

def update_session_stage(db: Session, session_id: int, stage: str):
    """Mark a stage as completed"""
    db_session = get_session_by_id(db, session_id)
    if not db_session:
        return None

    if stage == "quiz":
        db_session.quiz_completed = True
    elif stage == "coding":
        db_session.coding_completed = True
    elif stage == "audit":
        db_session.audit_completed = True
        # If all stages done, mark session complete
        if db_session.quiz_completed and db_session.coding_completed:
            db_session.status = "completed"
            db_session.completed_at = datetime.now()

    db.commit()
    db.refresh(db_session)
    return db_session


# ==================== RESULTS CRUD ====================

def save_assessment_result(db: Session, session_id: int, result_data: dict):
    """Save final assessment result"""
    db_result = models.AssessmentResult(
        session_id=session_id,
        employability_score=result_data["employability_score"],
        quiz_score=result_data["quiz_score"],
        coding_score=result_data["coding_score"],
        audit_score=result_data["audit_score"],
        feature_contributions=result_data["feature_contributions"],
        ai_feedback=result_data["ai_feedback"]
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

def get_session_quiz_results(db: Session, session_id: int) -> list:
    """Get all quiz responses for a session"""
    return (
        db.query(models.QuizResponse)
        .filter(models.QuizResponse.session_id == session_id)
        .all()
    )

def get_session_coding_submissions(db: Session, session_id: int) -> list:
    """Get all coding submissions for a session"""
    return (
        db.query(models.CodingSubmission)
        .filter(models.CodingSubmission.session_id == session_id)
        .all()
    )

def get_session_audit_submissions(db: Session, session_id: int) -> list:
    """Get all audit submissions for a session"""
    return (
        db.query(models.AuditSubmission)
        .filter(models.AuditSubmission.session_id == session_id)
        .all()
    )