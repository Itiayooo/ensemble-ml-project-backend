from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# ==================== QUIZ SCHEMAS ====================

class QuizQuestionCreate(BaseModel):
    """Used when SEEDING questions into the database"""
    question: str
    options: List[str]           # Must be exactly 4 options
    correct_answer: int          # Index 0-3
    difficulty: str = "medium"   # easy, medium, hard
    category: str = "general"

class QuizQuestionResponse(BaseModel):
    """What frontend RECEIVES - notice: no correct_answer!"""
    id: int
    question: str
    options: List[str]
    difficulty: str
    category: str

    class Config:
        from_attributes = True  # Allows reading from SQLAlchemy models

class QuizStartResponse(BaseModel):
    """Response when user starts the quiz"""
    session_id: int
    questions: List[QuizQuestionResponse]
    total_questions: int

class QuizAnswerItem(BaseModel):
    """A single quiz answer"""
    question_id: int
    selected_answer: int
    time_spent: int  # seconds

class QuizSubmission(BaseModel):
    """What frontend SENDS when submitting quiz"""
    session_id: int
    answers: List[QuizAnswerItem]

class QuizResultItem(BaseModel):
    """Result for a single question"""
    question_id: int
    is_correct: bool
    time_spent: int

class QuizSubmitResponse(BaseModel):
    """Response after quiz submission"""
    score: float               # percentage 0-100
    correct: int
    total: int
    results: List[QuizResultItem]
    passed: bool


# ==================== CODING SCHEMAS ====================

class CodingProblemCreate(BaseModel):
    """Used when SEEDING problems into the database"""
    title: str
    description: str
    difficulty: str = "medium"
    starter_code_python: Optional[str] = None
    starter_code_javascript: Optional[str] = None
    starter_code_java: Optional[str] = None
    test_cases: List[dict]      # [{input: ..., expected_output: ...}]
    constraints: Optional[List[str]] = None
    examples: Optional[List[dict]] = None

class CodingProblemResponse(BaseModel):
    """What frontend RECEIVES"""
    id: int
    title: str
    description: str
    difficulty: str
    starter_code_python: Optional[str] = None
    starter_code_javascript: Optional[str] = None
    starter_code_java: Optional[str] = None
    constraints: Optional[List[str]] = None
    examples: Optional[List[dict]] = None
    # Note: test_cases NOT included - frontend shouldn't see them

    class Config:
        from_attributes = True

class CodingStartResponse(BaseModel):
    """Response when user starts coding stage"""
    session_id: int
    problems: List[CodingProblemResponse]
    total_problems: int

class CodingSubmission(BaseModel):
    """What frontend SENDS"""
    session_id: int
    problem_id: int
    language: str
    code: str
    run_count: int = 0
    keystrokes: int = 0
    total_time: int             # seconds
    edit_events: Optional[List[dict]] = None

class CodingTestResult(BaseModel):
    """Result for a single test case"""
    test_case: int
    passed: bool
    expected: str
    actual: str

class CodingSubmitResponse(BaseModel):
    """Response after code submission"""
    problem_id: int
    tests_passed: int
    tests_total: int
    percentage: float
    test_results: List[CodingTestResult]
    code_metrics: dict          # lines_of_code, cyclomatic_complexity, etc.


# ==================== AUDIT SCHEMAS ====================

class AuditProblemCreate(BaseModel):
    """Used when SEEDING audit problems into the database"""
    title: str
    description: str
    difficulty: str = "medium"
    buggy_code_python: str
    buggy_code_javascript: Optional[str] = None
    known_issues: List[dict]    # [{type, severity, description, line_range}]
    test_cases: List[dict]

class AuditProblemResponse(BaseModel):
    """What frontend RECEIVES"""
    id: int
    title: str
    description: str
    difficulty: str
    buggy_code_python: str
    buggy_code_javascript: Optional[str] = None
    known_issues: List[dict]    # Frontend CAN see issues (it's a review task)

    class Config:
        from_attributes = True

class AuditStartResponse(BaseModel):
    """Response when user starts audit stage"""
    session_id: int
    problems: List[AuditProblemResponse]
    total_problems: int

class AuditSubmission(BaseModel):
    """What frontend SENDS"""
    session_id: int
    problem_id: int
    language: str
    modified_code: str
    edit_count: int = 0
    lines_changed: Optional[List[int]] = None
    edit_history: Optional[List[dict]] = None
    total_time: int

class AuditSubmitResponse(BaseModel):
    """Response after audit submission"""
    problem_id: int
    bugs_fixed: int
    bugs_total: int
    tests_passed: int
    tests_total: int
    efficiency_score: float
    feedback: str


# ==================== SESSION & USER SCHEMAS ====================

class UserCreate(BaseModel):
    """Create a new user"""
    email: str
    name: str

class UserResponse(BaseModel):
    """User data returned"""
    id: int
    email: str
    name: str

    class Config:
        from_attributes = True

class SessionStartRequest(BaseModel):
    """Request to start an assessment"""
    user_id: int

class SessionStatusResponse(BaseModel):
    """Current session status"""
    session_id: int
    quiz_completed: bool
    coding_completed: bool
    audit_completed: bool
    status: str


# ==================== RESULTS SCHEMAS ====================

class FeatureContribution(BaseModel):
    """Single SHAP-style feature contribution"""
    feature: str
    contribution: float
    color: str

class AIFeedback(BaseModel):
    """AI-generated feedback structure"""
    summary: str
    strengths: str
    improvements: str
    recommendation: str

class ResultsResponse(BaseModel):
    """Final assessment results"""
    session_id: int
    employability_score: float
    quiz_score: float
    coding_score: float
    audit_score: float
    feature_contributions: List[FeatureContribution]
    ai_feedback: AIFeedback
    percentile_rank: int
    category: str               # Hire, Consider, Develop