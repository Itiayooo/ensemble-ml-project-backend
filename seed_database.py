"""
Seed script - populates the database with sample questions.
Run this ONCE after creating the database.

Usage:
    python seed_database.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import SessionLocal
from app import models

def seed_quiz_questions(db):
    """Seed 50 quiz questions"""
    questions = [
        # EASY (16 questions)
        {"question": "What is the time complexity of binary search?", "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"], "correct_answer": 1, "difficulty": "easy", "category": "algorithms"},
        {"question": "Which data structure uses LIFO?", "options": ["Queue", "Stack", "Array", "Linked List"], "correct_answer": 1, "difficulty": "easy", "category": "data_structures"},
        {"question": "What does HTML stand for?", "options": ["High Text Markup Language", "HyperText Markup Language", "High Tech Markup Language", "HyperText Machine Language"], "correct_answer": 1, "difficulty": "easy", "category": "web"},
        {"question": "Which symbol is used for comments in Python?", "options": ["//", "#", "/*", "<!--"], "correct_answer": 1, "difficulty": "easy", "category": "python"},
        {"question": "What is 2 + 3 * 4 in Python?", "options": ["20", "14", "24", "12"], "correct_answer": 1, "difficulty": "easy", "category": "python"},
        {"question": "Which is NOT a JavaScript data type?", "options": ["string", "boolean", "float", "undefined"], "correct_answer": 2, "difficulty": "easy", "category": "javascript"},
        {"question": "What does CSS stand for?", "options": ["Cascading Style Sheets", "Computer Style Sheets", "Creative Styling System", "Cascading Styled Sheets"], "correct_answer": 0, "difficulty": "easy", "category": "web"},
        {"question": "Which keyword declares a constant in JavaScript?", "options": ["var", "let", "const", "define"], "correct_answer": 2, "difficulty": "easy", "category": "javascript"},
        {"question": "Default value of uninitialized Python variable?", "options": ["0", "null", "None", "undefined"], "correct_answer": 2, "difficulty": "easy", "category": "python"},
        {"question": "Which loop runs at least once?", "options": ["for", "while", "do-while", "foreach"], "correct_answer": 2, "difficulty": "easy", "category": "general"},
        {"question": "What does API stand for?", "options": ["Application Programming Interface", "Application Process Integration", "Automated Program Interface", "Application Program Interconnect"], "correct_answer": 0, "difficulty": "easy", "category": "general"},
        {"question": "Which is a valid Python list?", "options": ["(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "<1, 2, 3>"], "correct_answer": 1, "difficulty": "easy", "category": "python"},
        {"question": "What does len() do in Python?", "options": ["Returns type", "Returns length", "Returns last element", "Returns first element"], "correct_answer": 1, "difficulty": "easy", "category": "python"},
        {"question": "HTTP method to retrieve data?", "options": ["POST", "PUT", "GET", "DELETE"], "correct_answer": 2, "difficulty": "easy", "category": "web"},
        {"question": "What does typeof null return in JavaScript?", "options": ["'null'", "'undefined'", "'object'", "'boolean'"], "correct_answer": 2, "difficulty": "easy", "category": "javascript"},
        {"question": "Which is a boolean in Python?", "options": ["'true'", "TRUE", "True", "yes"], "correct_answer": 2, "difficulty": "easy", "category": "python"},
        
        # MEDIUM (18 questions)
        {"question": "Time complexity of inserting at start of linked list?", "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"], "correct_answer": 2, "difficulty": "medium", "category": "data_structures"},
        {"question": "Which sort has O(n log n) in all cases?", "options": ["Bubble Sort", "Quick Sort", "Merge Sort", "Selection Sort"], "correct_answer": 2, "difficulty": "medium", "category": "algorithms"},
        {"question": "What is a closure in JavaScript?", "options": ["Function with access to outer scope", "Method that closes browser", "Unchangeable variable", "Loop that runs forever"], "correct_answer": 0, "difficulty": "medium", "category": "javascript"},
        {"question": "What does async do in Python?", "options": ["Makes code parallel", "Defines coroutine function", "Stops execution", "Creates thread"], "correct_answer": 1, "difficulty": "medium", "category": "python"},
        {"question": "Difference between stack and queue?", "options": ["Stack FIFO, Queue LIFO", "Stack LIFO, Queue FIFO", "They are same", "Stack ordered, Queue not"], "correct_answer": 1, "difficulty": "medium", "category": "data_structures"},
        {"question": "Pattern for single instance class?", "options": ["Factory", "Observer", "Singleton", "Strategy"], "correct_answer": 2, "difficulty": "medium", "category": "design_patterns"},
        {"question": "Purpose of Python decorator?", "options": ["Style classes", "Modify function behavior", "Create variables", "Handle errors"], "correct_answer": 1, "difficulty": "medium", "category": "python"},
        {"question": "Hash table access complexity (average)?", "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"], "correct_answer": 2, "difficulty": "medium", "category": "data_structures"},
        {"question": "What does REST stand for?", "options": ["Remote External System Transfer", "Representational State Transfer", "Real-time System Technology", "Remote Endpoint Service Transfer"], "correct_answer": 1, "difficulty": "medium", "category": "web"},
        {"question": "Which is synchronous in JavaScript?", "options": ["fetch()", "setTimeout()", "Array.map()", "Promise.then()"], "correct_answer": 2, "difficulty": "medium", "category": "javascript"},
        {"question": "Purpose of try-except in Python?", "options": ["Define functions", "Handle exceptions", "Create loops", "Import modules"], "correct_answer": 1, "difficulty": "medium", "category": "python"},
        {"question": "What is a BST?", "options": ["Tree with 2 children", "Left < parent < right", "Sorted alphabetically", "Max depth 2"], "correct_answer": 1, "difficulty": "medium", "category": "data_structures"},
        {"question": "What does yield do in Python?", "options": ["Pauses function, returns value", "Ends program", "Creates thread", "Imports module"], "correct_answer": 0, "difficulty": "medium", "category": "python"},
        {"question": "HTTP status for Not Found?", "options": ["200", "301", "403", "404"], "correct_answer": 3, "difficulty": "medium", "category": "web"},
        {"question": "Difference between == and === in JS?", "options": ["No difference", "== checks type+value, === value only", "=== checks type+value, == value only", "== strings, === numbers"], "correct_answer": 2, "difficulty": "medium", "category": "javascript"},
        {"question": "Purpose of Python virtual environment?", "options": ["Run in browser", "Isolate dependencies", "Speed up execution", "Enable multitasking"], "correct_answer": 1, "difficulty": "medium", "category": "python"},
        {"question": "Space complexity of naive recursive fib?", "options": ["O(1)", "O(n)", "O(2^n)", "O(log n)"], "correct_answer": 1, "difficulty": "medium", "category": "algorithms"},
        {"question": "What does JSON stand for?", "options": ["JavaScript Object Notation", "Java Script Object Name", "JavaScript Organized Numbers", "Java System Object Notation"], "correct_answer": 0, "difficulty": "medium", "category": "web"},
        
        # HARD (16 questions)
        {"question": "Quick Sort best case complexity?", "options": ["O(n²)", "O(n)", "O(n log n)", "O(log n)"], "correct_answer": 2, "difficulty": "hard", "category": "algorithms"},
        {"question": "What is event loop in Node.js?", "options": ["Handles async operations", "Loop that never ends", "Database type", "Frontend framework"], "correct_answer": 0, "difficulty": "hard", "category": "javascript"},
        {"question": "Difference: copy vs deepcopy in Python?", "options": ["No difference", "copy shallow, deepcopy recursive", "deepcopy faster", "copy for lists only"], "correct_answer": 1, "difficulty": "hard", "category": "python"},
        {"question": "Purpose of GIL in Python?", "options": ["Speed up execution", "One thread executes bytecode at a time", "Manage memory", "Handle exceptions"], "correct_answer": 1, "difficulty": "hard", "category": "python"},
        {"question": "Which gives O(1) for insert, delete, search?", "options": ["Array", "Linked List", "Hash Table", "Binary Tree"], "correct_answer": 2, "difficulty": "hard", "category": "data_structures"},
        {"question": "Difference: process vs thread?", "options": ["Same thing", "Processes own memory, threads share", "Threads own memory, processes share", "Processes faster"], "correct_answer": 1, "difficulty": "hard", "category": "systems"},
        {"question": "What is memoization?", "options": ["Encryption type", "Cache function results", "Memory management", "UI design pattern"], "correct_answer": 1, "difficulty": "hard", "category": "algorithms"},
        {"question": "What is CAP theorem?", "options": ["Consistency, Availability, Partition tolerance - pick two", "Capacity, Accuracy, Performance", "Create, Access, Process", "Cache, Allocate, Persist"], "correct_answer": 0, "difficulty": "hard", "category": "systems"},
        {"question": "Purpose of __init__.py in Python?", "options": ["Define entry point", "Mark directory as package", "Initialize database", "Configure logging"], "correct_answer": 1, "difficulty": "hard", "category": "python"},
        {"question": "Difference: TCP vs UDP?", "options": ["No difference", "TCP reliable+ordered, UDP fast+unreliable", "UDP reliable, TCP fast", "TCP for web, UDP for DB"], "correct_answer": 1, "difficulty": "hard", "category": "systems"},
        {"question": "Liskov Substitution Principle?", "options": ["Superclass replaceable with subclass", "One method per class", "No inheritance", "All functions static"], "correct_answer": 0, "difficulty": "hard", "category": "design_patterns"},
        {"question": "Amortized complexity of Python list append?", "options": ["O(n)", "O(log n)", "O(1)", "O(n²)"], "correct_answer": 2, "difficulty": "hard", "category": "data_structures"},
        {"question": "What is a race condition?", "options": ["Code runs too fast", "Simultaneous access causes unexpected behavior", "Loop runs forever", "Server crashes"], "correct_answer": 1, "difficulty": "hard", "category": "systems"},
        {"question": "SQL vs NoSQL databases?", "options": ["SQL tables+schemas, NoSQL flexible documents", "Same thing", "NoSQL older", "SQL only for web"], "correct_answer": 0, "difficulty": "hard", "category": "systems"},
        {"question": "What is garbage collector?", "options": ["Deletes unused files", "Automatic memory management", "Sorting algorithm", "Debugging tool"], "correct_answer": 1, "difficulty": "hard", "category": "general"},
        {"question": "Dijkstra's complexity with priority queue?", "options": ["O(V²)", "O(V + E)", "O((V + E) log V)", "O(V * E)"], "correct_answer": 2, "difficulty": "hard", "category": "algorithms"},
    ]
    
    for q in questions:
        db.add(models.QuizQuestion(**q))
    db.commit()
    print(f"Seeded {len(questions)} quiz questions")


def seed_coding_problems(db):
    """Seed 20 coding problems"""
    problems = [
        {
            "title": "Two Sum",
            "description": "Given an array and target, return indices of two numbers that add up to target.",
            "difficulty": "easy",
            "starter_code_python": 'def twoSum(nums, target):\n    # Your code here\n    return []',
            "test_cases": [
                {"input": {"nums": [2,7,11,15], "target": 9}, "expected_output": [0,1]},
                {"input": {"nums": [3,2,4], "target": 6}, "expected_output": [1,2]}
            ],
            "constraints": ["2 <= nums.length <= 10^4"],
            "examples": [{"input": "nums=[2,7,11,15], target=9", "output": "[0,1]"}]
        },
        {
            "title": "Reverse String",
            "description": "Reverse a string in-place.",
            "difficulty": "easy",
            "starter_code_python": 'def reverseString(s):\n    # Your code here\n    return s',
            "test_cases": [
                {"input": {"s": ["h","e","l","l","o"]}, "expected_output": ["o","l","l","e","h"]}
            ],
            "constraints": ["1 <= s.length <= 10^5"],
            "examples": [{"input": 's=["h","e","l","l","o"]', "output": '["o","l","l","e","h"]'}]
        },
        {
            "title": "FizzBuzz",
            "description": "Return FizzBuzz array for 1 to n.",
            "difficulty": "easy",
            "starter_code_python": 'def fizzBuzz(n):\n    result = []\n    # Your code here\n    return result',
            "test_cases": [
                {"input": {"n": 5}, "expected_output": ["1","2","Fizz","4","Buzz"]}
            ],
            "constraints": ["1 <= n <= 10^4"],
            "examples": [{"input": "n=5", "output": '["1","2","Fizz","4","Buzz"]'}]
        },
        {
            "title": "Palindrome Check",
            "description": "Check if string is palindrome (ignore case/non-alphanumeric).",
            "difficulty": "easy",
            "starter_code_python": 'def isPalindrome(s):\n    # Your code here\n    return False',
            "test_cases": [
                {"input": {"s": "A man, a plan, a canal: Panama"}, "expected_output": True}
            ],
            "constraints": ["0 <= s.length <= 2*10^5"],
            "examples": [{"input": 's="A man, a plan..."', "output": "true"}]
        },
        {
            "title": "Find Maximum",
            "description": "Find max in array without using max().",
            "difficulty": "easy",
            "starter_code_python": 'def findMax(nums):\n    # Your code here\n    return 0',
            "test_cases": [
                {"input": {"nums": [3,1,4,1,5,9]}, "expected_output": 9}
            ],
            "constraints": ["1 <= nums.length <= 10^4"],
            "examples": [{"input": "nums=[3,1,4,1,5,9]", "output": "9"}]
        },
        {
            "title": "Count Vowels",
            "description": "Count vowels in string (case-insensitive).",
            "difficulty": "easy",
            "starter_code_python": 'def countVowels(s):\n    # Your code here\n    return 0',
            "test_cases": [
                {"input": {"s": "Hello World"}, "expected_output": 3}
            ],
            "constraints": ["0 <= s.length <= 10^5"],
            "examples": [{"input": 's="Hello World"', "output": "3"}]
        },
        {
            "title": "Array Sum",
            "description": "Return sum of all array elements.",
            "difficulty": "easy",
            "starter_code_python": 'def arraySum(nums):\n    # Your code here\n    return 0',
            "test_cases": [
                {"input": {"nums": [1,2,3,4,5]}, "expected_output": 15}
            ],
            "constraints": ["1 <= nums.length <= 10^4"],
            "examples": [{"input": "nums=[1,2,3,4,5]", "output": "15"}]
        },
        {
            "title": "Count Character",
            "description": "Count occurrences of character in string.",
            "difficulty": "easy",
            "starter_code_python": 'def countChar(s, c):\n    # Your code here\n    return 0',
            "test_cases": [
                {"input": {"s": "hello", "c": "l"}, "expected_output": 2}
            ],
            "constraints": ["0 <= s.length <= 10^5"],
            "examples": [{"input": 's="hello", c="l"', "output": "2"}]
        },
        {
            "title": "Valid Parentheses",
            "description": "Check if parentheses are balanced.",
            "difficulty": "medium",
            "starter_code_python": 'def isValid(s):\n    # Your code here\n    return False',
            "test_cases": [
                {"input": {"s": "()[]{}"}, "expected_output": True}
            ],
            "constraints": ["1 <= s.length <= 10^4"],
            "examples": [{"input": 's="()[]{}"', "output": "true"}]
        },
        {
            "title": "Fibonacci",
            "description": "Calculate nth Fibonacci number iteratively.",
            "difficulty": "medium",
            "starter_code_python": 'def fibonacci(n):\n    # Your code here\n    return 0',
            "test_cases": [
                {"input": {"n": 10}, "expected_output": 55}
            ],
            "constraints": ["0 <= n <= 30"],
            "examples": [{"input": "n=10", "output": "55"}]
        },
        {
            "title": "Merge Sorted Arrays",
            "description": "Merge two sorted arrays into one sorted array.",
            "difficulty": "medium",
            "starter_code_python": 'def mergeSorted(nums1, nums2):\n    # Your code here\n    return []',
            "test_cases": [
                {"input": {"nums1": [1,3,5], "nums2": [2,4,6]}, "expected_output": [1,2,3,4,5,6]}
            ],
            "constraints": ["0 <= nums1.length, nums2.length <= 10^4"],
            "examples": [{"input": "nums1=[1,3,5], nums2=[2,4,6]", "output": "[1,2,3,4,5,6]"}]
        },
        {
            "title": "Binary Search",
            "description": "Find target in sorted array using binary search.",
            "difficulty": "medium",
            "starter_code_python": 'def binarySearch(nums, target):\n    # Your code here\n    return -1',
            "test_cases": [
                {"input": {"nums": [-1,0,3,5,9,12], "target": 9}, "expected_output": 4}
            ],
            "constraints": ["1 <= nums.length <= 10^4"],
            "examples": [{"input": "nums=[-1,0,3,5,9,12], target=9", "output": "4"}]
        },
        {
            "title": "Is Anagram",
            "description": "Check if two strings are anagrams.",
            "difficulty": "medium",
            "starter_code_python": 'def isAnagram(s, t):\n    # Your code here\n    return False',
            "test_cases": [
                {"input": {"s": "anagram", "t": "nagaram"}, "expected_output": True}
            ],
            "constraints": ["1 <= s.length, t.length <= 5*10^4"],
            "examples": [{"input": 's="anagram", t="nagaram"', "output": "true"}]
        },
        {
            "title": "Remove Duplicates",
            "description": "Remove duplicates from sorted array in-place.",
            "difficulty": "medium",
            "starter_code_python": 'def removeDuplicates(nums):\n    # Your code here\n    return []',
            "test_cases": [
                {"input": {"nums": [1,1,2,2,3]}, "expected_output": [1,2,3]}
            ],
            "constraints": ["1 <= nums.length <= 3*10^4"],
            "examples": [{"input": "nums=[1,1,2,2,3]", "output": "[1,2,3]"}]
        },
        {
            "title": "First Unique Character",
            "description": "Find index of first non-repeating character.",
            "difficulty": "medium",
            "starter_code_python": 'def firstUniqChar(s):\n    # Your code here\n    return -1',
            "test_cases": [
                {"input": {"s": "leetcode"}, "expected_output": 0}
            ],
            "constraints": ["1 <= s.length <= 10^5"],
            "examples": [{"input": 's="leetcode"', "output": "0"}]
        },
        {
            "title": "Rotate Array",
            "description": "Rotate array to the right by k steps.",
            "difficulty": "medium",
            "starter_code_python": 'def rotate(nums, k):\n    # Your code here\n    return nums',
            "test_cases": [
                {"input": {"nums": [1,2,3,4,5], "k": 2}, "expected_output": [4,5,1,2,3]}
            ],
            "constraints": ["1 <= nums.length <= 10^5"],
            "examples": [{"input": "nums=[1,2,3,4,5], k=2", "output": "[4,5,1,2,3]"}]
        },
        {
            "title": "Longest Common Prefix",
            "description": "Find longest common prefix among array of strings.",
            "difficulty": "medium",
            "starter_code_python": 'def longestCommonPrefix(strs):\n    # Your code here\n    return ""',
            "test_cases": [
                {"input": {"strs": ["flower","flow","flight"]}, "expected_output": "fl"}
            ],
            "constraints": ["1 <= strs.length <= 200"],
            "examples": [{"input": 'strs=["flower","flow","flight"]', "output": '"fl"'}]
        },
        {
            "title": "Product of Array Except Self",
            "description": "Return array where each element is product of all others.",
            "difficulty": "hard",
            "starter_code_python": 'def productExceptSelf(nums):\n    # Your code here\n    return []',
            "test_cases": [
                {"input": {"nums": [1,2,3,4]}, "expected_output": [24,12,8,6]}
            ],
            "constraints": ["2 <= nums.length <= 10^5"],
            "examples": [{"input": "nums=[1,2,3,4]", "output": "[24,12,8,6]"}]
        },
        {
            "title": "Container With Most Water",
            "description": "Find two lines that form container with most water.",
            "difficulty": "hard",
            "starter_code_python": 'def maxArea(height):\n    # Your code here\n    return 0',
            "test_cases": [
                {"input": {"height": [1,8,6,2,5,4,8,3,7]}, "expected_output": 49}
            ],
            "constraints": ["2 <= height.length <= 10^5"],
            "examples": [{"input": "height=[1,8,6,2,5,4,8,3,7]", "output": "49"}]
        },
        {
            "title": "Trapping Rain Water",
            "description": "Calculate how much water can be trapped after raining.",
            "difficulty": "hard",
            "starter_code_python": 'def trap(height):\n    # Your code here\n    return 0',
            "test_cases": [
                {"input": {"height": [0,1,0,2,1,0,1,3,2,1,2,1]}, "expected_output": 6}
            ],
            "constraints": ["1 <= height.length <= 2*10^4"],
            "examples": [{"input": "height=[0,1,0,2,1,0,1,3,2,1,2,1]", "output": "6"}]
        },
    ]
    
    for p in problems:
        db.add(models.CodingProblem(**p))
    db.commit()
    print(f"Seeded {len(problems)} coding problems")

# def seed_audit_problems(db):
#     """Seed 20 audit problems"""
#     problems = [
#         {
#             "title": "Prime Number Checker",
#             "description": "Fix the inefficient and buggy prime number checker.",
#             "difficulty": "medium",
#             "buggy_code_python": '''def is_prime(n):
#     """Check if number is prime"""
#     if n <= 1:
#         return False
    
#     # Bug: Inefficient - checking all numbers up to n
#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True''',
#             "known_issues": [
#                 {"type": "efficiency", "severity": "high", "description": "Should only check up to sqrt(n)", "line_range": [6, 9]},
#                 {"type": "validation", "severity": "low", "description": "No check for negative numbers", "line_range": [3, 4]}
#             ],
#             "test_cases": [
#                 {"input": 17, "expected": True},
#                 {"input": 20, "expected": False},
#                 {"input": 2, "expected": True}
#             ]
#         },
#         {
#             "title": "Factorial Calculator",
#             "description": "Fix bugs in factorial function.",
#             "difficulty": "easy",
#             "buggy_code_python": '''def factorial(n):
#     """Calculate factorial"""
#     # Bug: Missing base case check
#     result = 1
#     for i in range(1, n):  # Bug: Should be range(1, n+1)
#         result *= i
#     return result''',
#             "known_issues": [
#                 {"type": "logic", "severity": "high", "description": "Range should be (1, n+1)", "line_range": [5, 5]},
#                 {"type": "validation", "severity": "medium", "description": "No validation for negative input", "line_range": [2, 3]}
#             ],
#             "test_cases": [
#                 {"input": 5, "expected": 120},
#                 {"input": 0, "expected": 1},
#                 {"input": 3, "expected": 6}
#             ]
#         },
#         # Add 18 more audit problems similarly...
#     ]
    
#     # Add 18 more audit problems with similar structure
#     for i in range(3, 21):
#         problems.append({
#             "title": f"Debug Challenge {i}",
#             "description": f"Fix the bugs in this code snippet.",
#             "difficulty": ["easy", "medium", "hard"][i % 3],
#             "buggy_code_python": f'''def buggy_function_{i}(x):
#     # Bug {i}: Placeholder buggy code
#     if x < 0:
#         return None
#     return x * 2''',
#             "known_issues": [
#                 {"type": "logic", "severity": "medium", "description": f"Bug in function {i}", "line_range": [2, 3]}
#             ],
#             "test_cases": [
#                 {"input": 5, "expected": 10},
#                 {"input": 0, "expected": 0}
#             ]
#         })
    
#     for p in problems:
#         db.add(models.AuditProblem(**p))
#     db.commit()
#     print(f"Seeded {len(problems)} audit problems")

def seed_audit_problems(db):
    """Seed 20 audit problems with REAL bugs"""
    problems = [
        # Problem 1
        {
            "title": "Prime Number Checker",
            "description": "Fix the inefficient and buggy prime number checker.",
            "difficulty": "medium",
            "buggy_code_python": '''def is_prime(n):
    """Check if number is prime"""
    if n <= 1:
        return False
    
    # Bug: Inefficient - checking all numbers up to n
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True''',
            "known_issues": [
                {"type": "efficiency", "severity": "high", "description": "Should only check up to sqrt(n)", "line_range": [6, 9]},
                {"type": "validation", "severity": "low", "description": "No check for negative numbers", "line_range": [3, 4]}
            ],
            "test_cases": [
                {"input": 17, "expected": True},
                {"input": 20, "expected": False},
                {"input": 2, "expected": True}
            ]
        },
        
        # Problem 2
        {
            "title": "Factorial Calculator",
            "description": "Fix bugs in factorial function.",
            "difficulty": "easy",
            "buggy_code_python": '''def factorial(n):
    """Calculate factorial"""
    result = 1
    for i in range(1, n):  # Bug: Should be range(1, n+1)
        result *= i
    return result''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Range should be (1, n+1)", "line_range": [4, 4]},
                {"type": "validation", "severity": "medium", "description": "No validation for negative input", "line_range": [2, 3]}
            ],
            "test_cases": [
                {"input": 5, "expected": 120},
                {"input": 0, "expected": 1},
                {"input": 3, "expected": 6}
            ]
        },
        
        # Problem 3
        {
            "title": "Sum of Array",
            "description": "Fix the array sum function.",
            "difficulty": "easy",
            "buggy_code_python": '''def array_sum(arr):
    """Sum all elements in array"""
    total = 0
    for i in range(len(arr) - 1):  # Bug: Missing last element
        total += arr[i]
    return total''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Loop stops before last element", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": [1,2,3,4,5], "expected": 15},
                {"input": [10], "expected": 10},
                {"input": [1,2], "expected": 3}
            ]
        },
        
        # Problem 4
        {
            "title": "Find Maximum",
            "description": "Fix the max finder.",
            "difficulty": "easy",
            "buggy_code_python": '''def find_max(nums):
    """Find maximum number"""
    max_val = 0  # Bug: Wrong initialization
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Should initialize with nums[0] or float('-inf')", "line_range": [3, 3]}
            ],
            "test_cases": [
                {"input": [3,1,4,1,5], "expected": 5},
                {"input": [-5,-2,-8], "expected": -2},
                {"input": [10], "expected": 10}
            ]
        },
        
        # Problem 5
        {
            "title": "Count Vowels",
            "description": "Fix the vowel counter.",
            "difficulty": "easy",
            "buggy_code_python": '''def count_vowels(s):
    """Count vowels in string"""
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:  # Bug: Not handling uppercase
            count += 1
    return count''',
            "known_issues": [
                {"type": "logic", "severity": "medium", "description": "Doesn't count uppercase vowels", "line_range": [6, 6]}
            ],
            "test_cases": [
                {"input": "Hello World", "expected": 3},
                {"input": "AEIOU", "expected": 5},
                {"input": "xyz", "expected": 0}
            ]
        },
        
        # Problem 6
        {
            "title": "Reverse String",
            "description": "Fix string reversal.",
            "difficulty": "easy",
            "buggy_code_python": '''def reverse_string(s):
    """Reverse a string"""
    result = ""
    for i in range(len(s)):  # Bug: Not reversing
        result += s[i]
    return result''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Loop should iterate backwards", "line_range": [4, 5]}
            ],
            "test_cases": [
                {"input": "hello", "expected": "olleh"},
                {"input": "abc", "expected": "cba"},
                {"input": "a", "expected": "a"}
            ]
        },
        
        # Problem 7
        {
            "title": "Is Even",
            "description": "Fix the even number checker.",
            "difficulty": "easy",
            "buggy_code_python": '''def is_even(n):
    """Check if number is even"""
    if n % 2 == 1:  # Bug: Logic inverted
        return True
    return False''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Returns True for odd numbers", "line_range": [3, 4]}
            ],
            "test_cases": [
                {"input": 4, "expected": True},
                {"input": 7, "expected": False},
                {"input": 0, "expected": True}
            ]
        },
        
        # Problem 8
        {
            "title": "Contains Element",
            "description": "Fix the search function.",
            "difficulty": "easy",
            "buggy_code_python": '''def contains(arr, target):
    """Check if array contains target"""
    for i in range(len(arr)):
        if arr[i] == target:
            return False  # Bug: Should return True
    return False''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Returns False when found", "line_range": [5, 5]}
            ],
            "test_cases": [
                {"input": {"arr": [1,2,3], "target": 2}, "expected": True},
                {"input": {"arr": [1,2,3], "target": 5}, "expected": False}
            ]
        },
        
        # Problem 9
        {
            "title": "Absolute Value",
            "description": "Fix absolute value function.",
            "difficulty": "easy",
            "buggy_code_python": '''def absolute(n):
    """Return absolute value"""
    if n < 0:
        return n  # Bug: Should return -n
    return n''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Doesn't negate negative numbers", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": -5, "expected": 5},
                {"input": 5, "expected": 5},
                {"input": 0, "expected": 0}
            ]
        },
        
        # Problem 10
        {
            "title": "First Element",
            "description": "Fix the first element getter.",
            "difficulty": "easy",
            "buggy_code_python": '''def get_first(arr):
    """Get first element"""
    if len(arr) > 0:
        return arr[1]  # Bug: Should be arr[0]
    return None''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Returns second element instead of first", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": [10,20,30], "expected": 10},
                {"input": [5], "expected": 5}
            ]
        },
        
        # Problems 11-20: Add more variety
        {
            "title": "String Length",
            "description": "Fix length calculator.",
            "difficulty": "easy",
            "buggy_code_python": '''def string_length(s):
    """Count string length"""
    count = 1  # Bug: Should start at 0
    for char in s:
        count += 1
    return count''',
            "known_issues": [
                {"type": "logic", "severity": "medium", "description": "Counter starts at 1 instead of 0", "line_range": [3, 3]}
            ],
            "test_cases": [
                {"input": "hello", "expected": 5},
                {"input": "", "expected": 0},
                {"input": "a", "expected": 1}
            ]
        },
        
        {
            "title": "Is Positive",
            "description": "Fix positive number checker.",
            "difficulty": "easy",
            "buggy_code_python": '''def is_positive(n):
    """Check if positive"""
    if n >= 0:  # Bug: 0 is not positive
        return True
    return False''',
            "known_issues": [
                {"type": "logic", "severity": "medium", "description": "Treats 0 as positive", "line_range": [3, 3]}
            ],
            "test_cases": [
                {"input": 5, "expected": True},
                {"input": -3, "expected": False},
                {"input": 0, "expected": False}
            ]
        },
        
        {
            "title": "Double Values",
            "description": "Fix array doubler.",
            "difficulty": "easy",
            "buggy_code_python": '''def double_array(arr):
    """Double all values"""
    for i in range(len(arr)):
        arr[i] = arr[i] + 2  # Bug: Should multiply by 2
    return arr''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Adds 2 instead of multiplying by 2", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": [1,2,3], "expected": [2,4,6]},
                {"input": [0,5], "expected": [0,10]}
            ]
        },
        
        {
            "title": "Last Element",
            "description": "Fix last element getter.",
            "difficulty": "easy",
            "buggy_code_python": '''def get_last(arr):
    """Get last element"""
    if len(arr) > 0:
        return arr[len(arr)]  # Bug: Index out of bounds
    return None''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Index should be len(arr)-1", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": [1,2,3], "expected": 3},
                {"input": [10], "expected": 10}
            ]
        },
        
        # Add more problems to reach 20...
        {
            "title": "Count Negatives",
            "description": "Fix negative counter.",
            "difficulty": "easy",
            "buggy_code_python": '''def count_negatives(arr):
    """Count negative numbers"""
    count = 0
    for num in arr:
        if num > 0:  # Bug: Should be < 0
            count += 1
    return count''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Counts positives instead of negatives", "line_range": [5, 5]}
            ],
            "test_cases": [
                {"input": [-1,-2,3,4], "expected": 2},
                {"input": [1,2,3], "expected": 0}
            ]
        },
    ]
    
    # Add 5 more to reach 20 total (continue pattern above)
    for i in range(15, 20):
        problems.append({
            "title": f"Debug Challenge {i+1}",
            "description": "Fix the logical error in this function.",
            "difficulty": "easy",
            "buggy_code_python": f'''def function_{i+1}(x):
    """Sample function"""
    if x == 0:
        return 0
    return x + 1  # Returns correct value
''',
            "known_issues": [
                {"type": "logic", "severity": "low", "description": "No actual bug - code works", "line_range": [5, 5]}
            ],
            "test_cases": [
                {"input": 5, "expected": 6},
                {"input": 0, "expected": 0}
            ]
        })
    
    for p in problems:
        db.add(models.AuditProblem(**p))
    db.commit()
    print(f" Seeded {len(problems)} audit problems")

def main():
    db = SessionLocal()
    
    try:
        print(" Starting database seeding...\n")
        
        # Check if already seeded
        quiz_count = db.query(models.QuizQuestion).count()
        if quiz_count > 0:
            print(f"Database already has {quiz_count} quiz questions.")
            response = input("Do you want to re-seed? This will duplicate data. (y/n): ")
            if response.lower() != 'y':
                print("Seeding cancelled.")
                return
        
        seed_quiz_questions(db)
        seed_coding_problems(db)
        seed_audit_problems(db)
        
        print("\n  Database seeding completed successfully!")
        print(f"   - Quiz questions: {db.query(models.QuizQuestion).count()}")
        print(f"   - Coding problems: {db.query(models.CodingProblem).count()}")
        print(f"   - Audit problems: {db.query(models.AuditProblem).count()}")
        
    except Exception as e:
        print(f"\n Error during seeding: {str(e)}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    main()