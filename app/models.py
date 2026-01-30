from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

# ==================== QUESTION BANKS ====================

class QuizQuestion(Base):
    __tablename__ = "quiz_questions"
    
    id = Column(Integer, primary_key=True, index=True)
    question = Column(Text, nullable=False)
    options = Column(JSON, nullable=False)  # List of 4 options
    correct_answer = Column(Integer, nullable=False)  # Index 0-3
    difficulty = Column(String(20), default="medium")  # easy, medium, hard
    category = Column(String(50), nullable=True)  # algorithms, data_structures, etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    responses = relationship("QuizResponse", back_populates="question")


class CodingProblem(Base):
    __tablename__ = "coding_problems"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String(20), default="medium")
    starter_code_python = Column(Text, nullable=True)
    starter_code_javascript = Column(Text, nullable=True)
    starter_code_java = Column(Text, nullable=True)
    test_cases = Column(JSON, nullable=False)  # List of {input, expected_output}
    constraints = Column(JSON, nullable=True)  # List of constraint strings
    examples = Column(JSON, nullable=True)  # List of example cases
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    submissions = relationship("CodingSubmission", back_populates="problem")


class AuditProblem(Base):
    __tablename__ = "audit_problems"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(String(20), default="medium")
    buggy_code_python = Column(Text, nullable=False)
    buggy_code_javascript = Column(Text, nullable=True)
    known_issues = Column(JSON, nullable=False)  # List of {type, severity, description, line_range}
    test_cases = Column(JSON, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    submissions = relationship("AuditSubmission", back_populates="problem")


# ==================== USER & SESSION ====================

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    sessions = relationship("AssessmentSession", back_populates="user")


class AssessmentSession(Base):
    __tablename__ = "assessment_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(String(50), default="in_progress")  # in_progress, completed
    quiz_completed = Column(Boolean, default=False)
    coding_completed = Column(Boolean, default=False)
    audit_completed = Column(Boolean, default=False)
    
    # Random question assignments (JSON arrays of IDs)
    assigned_quiz_questions = Column(JSON, nullable=True)
    assigned_coding_problems = Column(JSON, nullable=True)
    assigned_audit_problems = Column(JSON, nullable=True)
    
    started_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Relationships
    user = relationship("User", back_populates="sessions")
    quiz_responses = relationship("QuizResponse", back_populates="session")
    coding_submissions = relationship("CodingSubmission", back_populates="session")
    audit_submissions = relationship("AuditSubmission", back_populates="session")
    result = relationship("AssessmentResult", back_populates="session", uselist=False)


# ==================== RESPONSES & SUBMISSIONS ====================

class QuizResponse(Base):
    __tablename__ = "quiz_responses"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("assessment_sessions.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("quiz_questions.id"), nullable=False)
    selected_answer = Column(Integer, nullable=False)
    is_correct = Column(Boolean, nullable=False)
    time_spent = Column(Integer, nullable=False)  # seconds
    answered_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    session = relationship("AssessmentSession", back_populates="quiz_responses")
    question = relationship("QuizQuestion", back_populates="responses")


class CodingSubmission(Base):
    __tablename__ = "coding_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("assessment_sessions.id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("coding_problems.id"), nullable=False)
    language = Column(String(50), nullable=False)
    code = Column(Text, nullable=False)
    
    # Behavioral metadata
    run_count = Column(Integer, default=0)
    keystrokes = Column(Integer, default=0)
    total_time = Column(Integer, nullable=False)  # seconds
    edit_events = Column(JSON, nullable=True)  # Timestamped edit history
    
    # Test results
    tests_passed = Column(Integer, default=0)
    tests_total = Column(Integer, default=0)
    
    # Code metrics (calculated)
    lines_of_code = Column(Integer, nullable=True)
    cyclomatic_complexity = Column(Float, nullable=True)
    halstead_metrics = Column(JSON, nullable=True)
    
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    session = relationship("AssessmentSession", back_populates="coding_submissions")
    problem = relationship("CodingProblem", back_populates="submissions")


class AuditSubmission(Base):
    __tablename__ = "audit_submissions"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("assessment_sessions.id"), nullable=False)
    problem_id = Column(Integer, ForeignKey("audit_problems.id"), nullable=False)
    language = Column(String(50), nullable=False)
    original_code = Column(Text, nullable=False)
    modified_code = Column(Text, nullable=False)
    
    # Behavioral metadata
    edit_count = Column(Integer, default=0)
    lines_changed = Column(JSON, nullable=True)  # List of line numbers
    edit_history = Column(JSON, nullable=True)
    total_time = Column(Integer, nullable=False)  # seconds
    
    # Audit results
    bugs_fixed = Column(Integer, default=0)
    bugs_total = Column(Integer, default=0)
    tests_passed = Column(Integer, default=0)
    
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    session = relationship("AssessmentSession", back_populates="audit_submissions")
    problem = relationship("AuditProblem", back_populates="submissions")


# ==================== RESULTS ====================

class AssessmentResult(Base):
    __tablename__ = "assessment_results"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("assessment_sessions.id"), unique=True, nullable=False)
    
    # Overall score
    employability_score = Column(Float, nullable=False)
    
    # Stage scores
    quiz_score = Column(Float, nullable=False)
    coding_score = Column(Float, nullable=False)
    audit_score = Column(Float, nullable=False)
    
    # SHAP contributions
    feature_contributions = Column(JSON, nullable=True)
    
    # AI feedback
    ai_feedback = Column(JSON, nullable=True)  # {summary, strengths, improvements, recommendation}
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    session = relationship("AssessmentSession", back_populates="result")