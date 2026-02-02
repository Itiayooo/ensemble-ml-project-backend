from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
import subprocess
import json

router = APIRouter(prefix="/api/audit", tags=["Audit"])


# ==================== AUDIT ANALYSIS ====================

def analyze_audit(original_code: str, modified_code: str, known_issues: list) -> dict:
    """
    Compare original buggy code with the modified code.
    Detect which bugs the student fixed.
    """
    bugs_fixed = 0
    bug_details = []

    for issue in known_issues:
        fixed = False
        issue_type = issue.get("type", "")
        severity = issue.get("severity", "")

        # Check for efficiency fix (sqrt optimization)
        if issue_type == "efficiency":
            if any(keyword in modified_code for keyword in ["sqrt", "**0.5", "** 0.5", "Math.sqrt"]):
                fixed = True

        # Check for off-by-one fix (range includes limit)
        elif issue_type == "logic":
            if "limit + 1" in modified_code or "limit+1" in modified_code:
                fixed = True

        # Check for input validation
        elif issue_type == "validation":
            if any(keyword in modified_code for keyword in ["< 0", "<0", "negative", "ValueError"]):
                fixed = True

        if fixed:
            bugs_fixed += 1

        bug_details.append({
            "issue_type": issue_type,
            "severity": severity,
            "fixed": fixed,
            "description": issue.get("description", "")
        })

    return {
        "bugs_fixed": bugs_fixed,
        "bugs_total": len(known_issues),
        "bug_details": bug_details
    }


def run_audit_tests(modified_code: str, test_cases: list) -> dict:
    """Run test cases against modified code"""
    passed = 0
    total = len(test_cases)

    for test in test_cases:
        test_script = f"""
import math

{modified_code}

try:
    result = is_prime({json.dumps(test['input'])})
    expected = {json.dumps(test['expected'])}
    if result == expected:
        print("PASS")
    else:
        print("FAIL")
except Exception as e:
    print(f"ERROR: {{e}}")
"""
        try:
            process = subprocess.run(
                ["python", "-c", test_script],
                capture_output=True,
                text=True,
                timeout=5
            )
            if process.stdout.strip() == "PASS":
                passed += 1
        except (subprocess.TimeoutExpired, Exception):
            continue

    return {"passed": passed, "total": total}


# def calculate_edit_metrics(original: str, modified: str, edit_count: int) -> float:
#     """
#     Calculate edit efficiency score.
#     Fewer, more targeted edits = higher score.
#     """
#     orig_lines = original.split('\n')
#     mod_lines = modified.split('\n')

#     # Count actually changed lines
#     changed = 0
#     for i in range(min(len(orig_lines), len(mod_lines))):
#         if orig_lines[i] != mod_lines[i]:
#             changed += 1

#     # Account for added/removed lines
#     changed += abs(len(orig_lines) - len(mod_lines))

#     # Efficiency: fewer changes for more fixes = better
#     # Perfect score if minimal changes made
#     if changed == 0:
#         return 0.0  # Nothing was changed

#     efficiency = max(0, min(100, 100 - (changed * 5) - (edit_count * 0.5)))
#     return round(efficiency, 2)

def calculate_audit_score(bugs_fixed: int, bugs_total: int, lines_changed: int, edit_count: int) -> float:
    """
    Calculate overall audit score.
    - 0% if no bugs fixed
    - Higher score for fixing more bugs with fewer edits
    """
    if bugs_fixed == 0:
        return 0.0
    
    # Base score from bug fix rate (0-70 points)
    base_score = (bugs_fixed / bugs_total) * 70
    
    # Efficiency bonus (0-30 points)
    # Ideal: ~3 edits per bug, ~5 lines per bug
    expected_edits = bugs_fixed * 3
    expected_lines = bugs_fixed * 5
    
    edit_efficiency = max(0, 15 - abs(edit_count - expected_edits))
    line_efficiency = max(0, 15 - abs(lines_changed - expected_lines))
    
    total_score = base_score + edit_efficiency + line_efficiency
    
    return round(min(100, total_score), 2)

def generate_audit_feedback(bug_analysis: dict, test_results: dict, efficiency: float) -> str:
    """Generate human-readable feedback"""
    feedback_parts = []

    bugs_fixed = bug_analysis["bugs_fixed"]
    bugs_total = bug_analysis["bugs_total"]

    # Bug fix feedback
    if bugs_fixed == bugs_total:
        feedback_parts.append("Excellent! You identified and fixed all the bugs in the code.")
    elif bugs_fixed > 0:
        feedback_parts.append(f"You fixed {bugs_fixed} out of {bugs_total} bugs.")
        # Tell them which ones they missed
        for detail in bug_analysis["bug_details"]:
            if not detail["fixed"]:
                feedback_parts.append(f"Missed: {detail['description']}")
    else:
        feedback_parts.append("No bugs were fixed. Review the code more carefully.")

    # Test results feedback
    if test_results["passed"] == test_results["total"]:
        feedback_parts.append("All test cases pass.")
    else:
        feedback_parts.append(
            f"Only {test_results['passed']}/{test_results['total']} test cases pass. "
            f"Check your logic for edge cases."
        )

    # Efficiency feedback
    if efficiency > 70:
        feedback_parts.append("Your edits were precise and targeted.")
    elif efficiency > 40:
        feedback_parts.append("Consider making more focused edits next time.")
    else:
        feedback_parts.append("Try to be more surgical with your code changes.")

    return " ".join(feedback_parts)


# ==================== API ENDPOINTS ====================

@router.get("/start/{session_id}", response_model=schemas.AuditStartResponse)
def start_audit(session_id: int, db: Session = Depends(get_db)):
    """Fetch 1 random audit problem"""
    session = crud.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if not session.coding_completed:
        raise HTTPException(status_code=400, detail="Must complete coding stage first")

    if session.audit_completed:
        raise HTTPException(status_code=400, detail="Audit stage already completed")

    problems = crud.get_random_audit_problems(db, count=1)

    if not problems:
        raise HTTPException(status_code=500, detail="No audit problems in database. Run the seed script first.")

    return {
        "session_id": session_id,
        "problems": problems,
        "total_problems": len(problems)
    }


@router.post("/test")
def test_audit(submission: schemas.AuditSubmission, db: Session = Depends(get_db)):
    """Test the modified code WITHOUT saving."""
    problem = crud.get_audit_problem_by_id(db, submission.problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Run tests
    test_results = run_audit_tests(submission.modified_code, problem.test_cases)

    # Analyze bug fixes
    bug_analysis = analyze_audit(
        problem.buggy_code_python,
        submission.modified_code,
        problem.known_issues
    )

    # Calculate efficiency
    efficiency = calculate_audit_score(
        bugs_fixed=bug_analysis["bugs_fixed"],
        bugs_total=bug_analysis["bugs_total"],
        lines_changed=len(submission.lines_changed or []),
        edit_count=submission.edit_count
    )

    return {
        "test_results": test_results,
        "bug_analysis": bug_analysis,
        "efficiency_score": efficiency
    }
# def test_audit(submission: schemas.AuditSubmission, db: Session = Depends(get_db)):
#     """
#     Test the modified code WITHOUT saving.
#     User can call this multiple times.
#     """
#     problem = crud.get_audit_problem_by_id(db, submission.problem_id)
#     if not problem:
#         raise HTTPException(status_code=404, detail="Problem not found")

#     # Run tests
#     test_results = run_audit_tests(submission.modified_code, problem.test_cases)

#     # Analyze bug fixes
#     bug_analysis = analyze_audit(
#         problem.buggy_code_python,
#         submission.modified_code,
#         problem.known_issues
#     )

#     # Calculate efficiency
#     efficiency = calculate_edit_metrics(
#         problem.buggy_code_python,
#         submission.modified_code,
#         submission.edit_count
#     )

#     return {
#         "test_results": test_results,
#         "bug_analysis": bug_analysis,
#         "efficiency_score": efficiency
#     }


@router.post("/submit", response_model=schemas.AuditSubmitResponse)
def submit_audit(submission: schemas.AuditSubmission, db: Session = Depends(get_db)):
    """Final submission"""
    session = crud.get_session_by_id(db, submission.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if session.audit_completed:
        raise HTTPException(status_code=400, detail="Audit stage already completed")

    problem = crud.get_audit_problem_by_id(db, submission.problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Run tests
    test_results = run_audit_tests(submission.modified_code, problem.test_cases)

    # Analyze bug fixes
    bug_analysis = analyze_audit(
        problem.buggy_code_python,
        submission.modified_code,
        problem.known_issues
    )

    # Calculate score (FIXED - now returns 0 if no bugs fixed)
    efficiency = calculate_audit_score(
        bugs_fixed=bug_analysis["bugs_fixed"],
        bugs_total=bug_analysis["bugs_total"],
        lines_changed=len(submission.lines_changed or []),
        edit_count=submission.edit_count
    )

    # Generate feedback
    feedback = generate_audit_feedback(bug_analysis, test_results, efficiency)

    # Save to database
    crud.save_audit_submission(
        db,
        submission,
        audit_results={
            "original_code": problem.buggy_code_python,
            "bugs_fixed": bug_analysis["bugs_fixed"],
            "bugs_total": bug_analysis["bugs_total"],
            "tests_passed": test_results["passed"]
        }
    )

    # Mark stage complete
    crud.update_session_stage(db, submission.session_id, "audit")

    return {
        "problem_id": submission.problem_id,
        "bugs_fixed": bug_analysis["bugs_fixed"],
        "bugs_total": bug_analysis["bugs_total"],
        "tests_passed": test_results["passed"],
        "tests_total": test_results["total"],
        "efficiency_score": efficiency,  # Now this will be 0 if no bugs fixed
        "feedback": feedback
    }

# @router.post("/submit", response_model=schemas.AuditSubmitResponse)
# def submit_audit(submission: schemas.AuditSubmission, db: Session = Depends(get_db)):
    """
    Final submission - analyzes audit, saves to DB, marks stage complete.
    """
    session = crud.get_session_by_id(db, submission.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if session.audit_completed:
        raise HTTPException(status_code=400, detail="Audit stage already completed")

    problem = crud.get_audit_problem_by_id(db, submission.problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Run tests
    test_results = run_audit_tests(submission.modified_code, problem.test_cases)

    # Analyze bug fixes
    bug_analysis = analyze_audit(
        problem.buggy_code_python,
        submission.modified_code,
        problem.known_issues
    )

    # Calculate efficiency
    efficiency = calculate_edit_metrics(
        problem.buggy_code_python,
        submission.modified_code,
        submission.edit_count
    )

    # Generate feedback
    feedback = generate_audit_feedback(bug_analysis, test_results, efficiency)

    # Save to database
    crud.save_audit_submission(
        db,
        submission,
        audit_results={
            "original_code": problem.buggy_code_python,
            "bugs_fixed": bug_analysis["bugs_fixed"],
            "bugs_total": bug_analysis["bugs_total"],
            "tests_passed": test_results["passed"]
        }
    )

    # Mark stage complete
    crud.update_session_stage(db, submission.session_id, "audit")

    return {
        "problem_id": submission.problem_id,
        "bugs_fixed": bug_analysis["bugs_fixed"],
        "bugs_total": bug_analysis["bugs_total"],
        "tests_passed": test_results["passed"],
        "tests_total": test_results["total"],
        "efficiency_score": efficiency,
        "feedback": feedback
    }