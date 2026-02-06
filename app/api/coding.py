from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud, schemas
import subprocess
import json
import traceback

router = APIRouter(prefix="/api/coding", tags=["Coding"])


# ==================== CODE EXECUTION ====================

# def execute_python_code(code: str, test_cases: list) -> list:
#     """
#     Safely execute Python code against test cases.
#     Uses subprocess with timeout to prevent infinite loops.
#     """
#     results = []

#     for i, test in enumerate(test_cases):
#         # Build a script that runs user code + test case
#         test_script = f"""
# import sys
# import json

# # User's code
# {code}

# # Run test
# try:
#     input_data = {json.dumps(test['input'])}
    
#     # Call the function dynamically
#     func_name = list(input_data.keys())[0] if isinstance(input_data, dict) else None
    
#     # For Two Sum style problems
#     if 'nums' in input_data and 'target' in input_data:
#         result = twoSum(input_data['nums'], input_data['target'])
#     # For generic single-argument problems  
#     elif len(input_data) == 1:
#         key = list(input_data.keys())[0]
#         result = eval(list(globals().keys())[-1])(input_data[key])
#     else:
#         result = None
        
#     print(json.dumps(result))
# except Exception as e:
#     print(json.dumps({{"error": str(e)}}))
# """
#         try:
#             process = subprocess.run(
#                 ["python", "-c", test_script],
#                 capture_output=True,
#                 text=True,
#                 timeout=5  # 5 second timeout
#             )

#             if process.returncode == 0:
#                 actual_output = process.stdout.strip()
#                 expected = json.dumps(test['expected_output'])

#                 # Compare outputs
#                 passed = actual_output == expected

#                 results.append({
#                     "test_case": i + 1,
#                     "passed": passed,
#                     "expected": expected,
#                     "actual": actual_output
#                 })
#             else:
#                 results.append({
#                     "test_case": i + 1,
#                     "passed": False,
#                     "expected": json.dumps(test['expected_output']),
#                     "actual": f"Error: {process.stderr.strip()}"
#                 })

#         except subprocess.TimeoutExpired:
#             results.append({
#                 "test_case": i + 1,
#                 "passed": False,
#                 "expected": json.dumps(test['expected_output']),
#                 "actual": "Error: Time Limit Exceeded (5s)"
#             })
#         except Exception as e:
#             results.append({
#                 "test_case": i + 1,
#                 "passed": False,
#                 "expected": json.dumps(test['expected_output']),
#                 "actual": f"Error: {str(e)}"
#             })

#     return results

def execute_python_code(code: str, test_cases: list) -> list:
    """
    Safely execute Python code against test cases.
    Uses subprocess with timeout to prevent infinite loops.
    """
    results = []

    # Extract function name from code
    import re
    func_match = re.search(r'def (\w+)\(', code)
    if not func_match:
        return [{
            "test_case": 1,
            "passed": False,
            "expected": "",
            "actual": "Error: No function definition found in code"
        }]
    
    func_name = func_match.group(1)

    for i, test in enumerate(test_cases):
        # Build a script that runs user code + test case
        test_script = f"""
import sys
import json

# User's code
{code}

try:
    # Get test input
    test_input = {repr(test['input'])}
    
    # Call function with unpacked arguments
    result = {func_name}(**test_input)
    
    # Print result as JSON
    print(json.dumps(result))
    
except Exception as e:
    # Print error to stderr
    import traceback
    print(json.dumps({{"error": str(e)}}), file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)
"""
        
        try:
            process = subprocess.run(
                ["python", "-c", test_script],
                capture_output=True,
                text=True,
                timeout=5  # 5 second timeout
            )

            if process.returncode == 0:
                actual_output = process.stdout.strip()
                try:
                    actual = json.loads(actual_output)
                except json.JSONDecodeError:
                    actual = actual_output
                
                expected = test['expected_output']
                
                # Compare outputs (handle lists/dicts)
                passed = (actual == expected)

                results.append({
                    "test_case": i + 1,
                    "passed": passed,
                    "expected": str(expected),
                    "actual": str(actual)
                })
            else:
                error_output = process.stderr.strip()
                results.append({
                    "test_case": i + 1,
                    "passed": False,
                    "expected": str(test['expected_output']),
                    "actual": f"Error: {error_output.split('Error:')[-1].strip() if 'Error:' in error_output else error_output[:100]}"
                })

        except subprocess.TimeoutExpired:
            results.append({
                "test_case": i + 1,
                "passed": False,
                "expected": str(test['expected_output']),
                "actual": "Error: Time Limit Exceeded (5s)"
            })
        except Exception as e:
            results.append({
                "test_case": i + 1,
                "passed": False,
                "expected": str(test['expected_output']),
                "actual": f"Error: {str(e)}"
            })

    return results

def extract_code_metrics(code: str) -> dict:
    """Extract code metrics using radon library"""
    try:
        from radon.complexity import cc_visit
        from radon.metrics import mi_compute
        from radon.raw import analyze

        # Cyclomatic complexity
        complexity_results = cc_visit(code)
        avg_complexity = (
            sum(r.complexity for r in complexity_results) / len(complexity_results)
            if complexity_results else 1.0
        )

        # Raw metrics (lines of code, etc.)
        raw = analyze(code)

        return {
            "lines_of_code": raw.loc,
            "logical_lines": raw.lloc,
            "blank_lines": raw.blank,
            "comment_lines": raw.comments,
            "cyclomatic_complexity": round(avg_complexity, 2),
            "halstead_metrics": {
                "functions_count": len(complexity_results)
            }
        }

    except Exception as e:
        # Fallback if radon fails
        lines = code.split('\n')
        return {
            "lines_of_code": len(lines),
            "logical_lines": len([l for l in lines if l.strip()]),
            "blank_lines": len([l for l in lines if not l.strip()]),
            "comment_lines": len([l for l in lines if l.strip().startswith('#')]),
            "cyclomatic_complexity": 1.0,
            "halstead_metrics": {}
        }


# ==================== API ENDPOINTS ====================

@router.get("/start/{session_id}", response_model=schemas.CodingStartResponse)
def start_coding(session_id: int, db: Session = Depends(get_db)):
    """Fetch 1 random coding problem"""
    session = crud.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if not session.quiz_completed:
        raise HTTPException(status_code=400, detail="Must complete quiz first")

    if session.coding_completed:
        raise HTTPException(status_code=400, detail="Coding stage already completed")

    problems = crud.get_random_coding_problems(db, count=1)

    if not problems:
        raise HTTPException(status_code=500, detail="No coding problems in database. Run the seed script first.")

    return {
        "session_id": session_id,
        "problems": problems,
        "total_problems": len(problems)
    }


@router.post("/run", response_model=schemas.CodingSubmitResponse)
def run_code(submission: schemas.CodingSubmission, db: Session = Depends(get_db)):
    """
    Run user code against test cases WITHOUT saving.
    User can call this multiple times (run button).
    """
    problem = crud.get_coding_problem_by_id(db, submission.problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Only support Python execution for now
    if submission.language != "python":
        raise HTTPException(status_code=400, detail="Only Python execution is supported currently")

    # Execute code
    test_results = execute_python_code(submission.code, problem.test_cases)

    # Extract metrics
    code_metrics = extract_code_metrics(submission.code)

    passed = sum(1 for r in test_results if r["passed"])
    total = len(test_results)

    return {
        "problem_id": submission.problem_id,
        "tests_passed": passed,
        "tests_total": total,
        "percentage": round((passed / total) * 100, 2) if total > 0 else 0,
        "test_results": test_results,
        "code_metrics": code_metrics
    }


@router.post("/submit", response_model=schemas.CodingSubmitResponse)
def submit_coding(submission: schemas.CodingSubmission, db: Session = Depends(get_db)):
    """
    Final submission - runs tests, saves to DB, marks stage complete.
    """
    session = crud.get_session_by_id(db, submission.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    if session.coding_completed:
        raise HTTPException(status_code=400, detail="Coding stage already completed")

    problem = crud.get_coding_problem_by_id(db, submission.problem_id)
    if not problem:
        raise HTTPException(status_code=404, detail="Problem not found")

    # Execute code
    test_results = execute_python_code(submission.code, problem.test_cases)

    # Extract metrics
    code_metrics = extract_code_metrics(submission.code)

    passed = sum(1 for r in test_results if r["passed"])
    total = len(test_results)

    # Save to database
    crud.save_coding_submission(
        db,
        submission,
        test_results={"passed": passed, "total": total},
        code_metrics=code_metrics
    )

    # Mark stage complete
    crud.update_session_stage(db, submission.session_id, "coding")

    return {
        "problem_id": submission.problem_id,
        "tests_passed": passed,
        "tests_total": total,
        "percentage": round((passed / total) * 100, 2) if total > 0 else 0,
        "test_results": test_results,
        "code_metrics": code_metrics
    }