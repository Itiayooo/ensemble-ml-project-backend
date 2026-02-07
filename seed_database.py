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


def seed_audit_problems(db):
    """Seed 20 audit problems with REAL bugs"""
    problems = [
        # EASY (5 problems)
        {
            "title": "Factorial Bug",
            "description": "This function calculates factorial but has an off-by-one error. Find and fix it.",
            "difficulty": "easy",
            "buggy_code_python": '''def factorial(n):
    """Calculate factorial of n"""
    if n <= 0:
        return 1
    result = 1
    for i in range(1, n):  
        result *= i
    return result

# Test
print(factorial(5))  # Should be 120''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Range excludes n itself", "line_range": [5, 5]}
            ],
            "test_cases": [
                {"input": 5, "expected": 120},
                {"input": 3, "expected": 6},
                {"input": 0, "expected": 1}
            ]
        },
        {
            "title": "List Average Bug",
            "description": "This function calculates average but crashes on empty lists. Add proper error handling.",
            "difficulty": "easy",
            "buggy_code_python": '''def calculate_average(numbers):
    """Calculate average of numbers"""
    total = sum(numbers)
    return total / len(numbers)  

# Test
print(calculate_average([10, 20, 30]))''',
            "known_issues": [
                {"type": "validation", "severity": "high", "description": "No check for empty list", "line_range": [3, 4]}
            ],
            "test_cases": [
                {"input": [10, 20, 30], "expected": 20.0},
                {"input": [5], "expected": 5.0},
                {"input": [], "expected": 0}
            ]
        },
        {
            "title": "String Reversal Bug",
            "description": "This function should reverse a string but has incorrect indexing.",
            "difficulty": "easy",
            "buggy_code_python": '''def reverse_string(s):
    """Reverse a string"""
    result = ""
    for i in range(len(s)):  
        result += s[i]
    return result

# Test
print(reverse_string("hello"))  # Should be "olleh"''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Iterates forward instead of backward", "line_range": [4, 5]}
            ],
            "test_cases": [
                {"input": "hello", "expected": "olleh"},
                {"input": "abc", "expected": "cba"},
                {"input": "a", "expected": "a"}
            ]
        },
        {
            "title": "Max Finder Bug",
            "description": "This function finds maximum but fails on negative numbers.",
            "difficulty": "easy",
            "buggy_code_python": '''def find_max(numbers):
    """Find maximum number in list"""
    max_num = 0  
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test
print(find_max([3, 7, 2, 9]))''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Incorrect initialization - fails on all-negative lists", "line_range": [3, 3]}
            ],
            "test_cases": [
                {"input": [3, 7, 2, 9], "expected": 9},
                {"input": [-5, -1, -10], "expected": -1},
                {"input": [100], "expected": 100}
            ]
        },
        {
            "title": "Duplicate Counter Bug",
            "description": "This function counts duplicates but has a logic error.",
            "difficulty": "easy",
            "buggy_code_python": '''def count_duplicates(arr):
    """Count duplicate elements"""
    seen = set()
    duplicates = 0
    for item in arr:
        if item in seen:
            duplicates += 1
        seen.add(item)  
    return duplicates

# Test
print(count_duplicates([1, 2, 2, 3, 3, 3]))''',
            "known_issues": [
                {"type": "logic", "severity": "medium", "description": "Adds to set after checking, causing off-by-one", "line_range": [6, 8]}
            ],
            "test_cases": [
                {"input": [1, 2, 2, 3, 3, 3], "expected": 3},
                {"input": [1, 1, 1], "expected": 2},
                {"input": [1, 2, 3], "expected": 0}
            ]
        },

        # MEDIUM (5 problems)
        {
            "title": "Inefficient Prime Checker",
            "description": "This prime checker works but is extremely slow. Optimize it to check only up to sqrt(n).",
            "difficulty": "medium",
            "buggy_code_python": '''def is_prime(n):
    """Check if n is prime"""
    if n < 2:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

# Test
print(is_prime(17))''',
            "known_issues": [
                {"type": "efficiency", "severity": "high", "description": "Checks all numbers up to n instead of sqrt(n)", "line_range": [5, 5]}
            ],
            "test_cases": [
                {"input": 17, "expected": True},
                {"input": 20, "expected": False},
                {"input": 2, "expected": True}
            ]
        },
        {
            "title": "Binary Search Bug",
            "description": "This binary search has a subtle overflow bug in the midpoint calculation.",
            "difficulty": "medium",
            "buggy_code_python": '''def binary_search(arr, target):
    """Binary search for target in sorted array"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test
print(binary_search([1, 3, 5, 7, 9], 5))''',
            "known_issues": [
                {"type": "efficiency", "severity": "medium", "description": "Potential integer overflow, should use left + (right-left)//2", "line_range": [5, 5]}
            ],
            "test_cases": [
                {"input": {"arr": [1, 3, 5, 7, 9], "target": 5}, "expected": 2},
                {"input": {"arr": [1, 3, 5, 7, 9], "target": 1}, "expected": 0},
                {"input": {"arr": [1, 3, 5, 7, 9], "target": 10}, "expected": -1}
            ]
        },
        {
            "title": "Palindrome Checker Bug",
            "description": "This palindrome checker fails on strings with mixed case and spaces.",
            "difficulty": "medium",
            "buggy_code_python": '''def is_palindrome(s):
    """Check if string is palindrome"""
    
    return s == s[::-1]

# Test
print(is_palindrome("racecar"))  # True
print(is_palindrome("A man a plan a canal Panama"))  # Should be True''',
            "known_issues": [
                {"type": "validation", "severity": "medium", "description": "Doesn't normalize case or remove spaces", "line_range": [3, 4]}
            ],
            "test_cases": [
                {"input": "racecar", "expected": True},
                {"input": "A man a plan a canal Panama", "expected": True},
                {"input": "hello", "expected": False}
            ]
        },
        {
            "title": "Merge Sort Bug",
            "description": "This merge sort has an index error in the merge step.",
            "difficulty": "medium",
            "buggy_code_python": '''def merge_sort(arr):
    """Sort array using merge sort"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    return result

# Test
print(merge_sort([5, 2, 8, 1, 9]))''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Missing code to add remaining elements from left/right", "line_range": [18, 18]}
            ],
            "test_cases": [
                {"input": [5, 2, 8, 1, 9], "expected": [1, 2, 5, 8, 9]},
                {"input": [3, 1, 2], "expected": [1, 2, 3]},
                {"input": [1], "expected": [1]}
            ]
        },
        {
            "title": "Fibonacci Bug",
            "description": "This fibonacci function has incorrect base cases.",
            "difficulty": "medium",
            "buggy_code_python": '''def fibonacci(n):
    """Calculate nth fibonacci number"""
    if n <= 1:  
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

# Test
print(fibonacci(5))  # Should be 5 (0,1,1,2,3,5)
print(fibonacci(0))  # Should be 0''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Returns 1 for n=0, should return 0", "line_range": [3, 4]}
            ],
            "test_cases": [
                {"input": 5, "expected": 5},
                {"input": 0, "expected": 0},
                {"input": 1, "expected": 1}
            ]
        },

        # HARD (5 problems)
        {
            "title": "LRU Cache Bug",
            "description": "This LRU cache has a subtle bug in the eviction logic.",
            "difficulty": "hard",
            "buggy_code_python": '''class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1
    
    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)  
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)

# Test
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))''',
            "known_issues": [
                {"type": "logic", "severity": "medium", "description": "Order of operations in put() can cause issues", "line_range": [17, 19]}
            ],
            "test_cases": [
                {"input": {"operations": ["put", "put", "get"], "args": [[1,1], [2,2], [1]]}, "expected": 1}
            ]
        },
        {
            "title": "Deadlock Risk",
            "description": "This code has a potential deadlock when acquiring multiple locks.",
            "difficulty": "hard",
            "buggy_code_python": '''import threading

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()
    
    def transfer(self, other, amount):
       
        self.lock.acquire()
        other.lock.acquire()
        
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
        
        self.lock.release()
        other.lock.release()

# Test
acc1 = BankAccount(100)
acc2 = BankAccount(50)
acc1.transfer(acc2, 30)
print(acc1.balance, acc2.balance)''',
            "known_issues": [
                {"type": "concurrency", "severity": "high", "description": "Lock ordering can cause deadlock", "line_range": [9, 10]}
            ],
            "test_cases": [
                {"input": {"initial": [100, 50], "transfer": 30}, "expected": [70, 80]}
            ]
        },
        {
            "title": "Memory Leak in Generator",
            "description": "This generator has a memory leak due to circular reference.",
            "difficulty": "hard",
            "buggy_code_python": '''class DataProcessor:
    def __init__(self):
        self.data = []
        self.processor = self.process_data()  
    
    def process_data(self):
        while True:
            if self.data:
                item = self.data.pop(0)
                yield item * 2

# Test
processor = DataProcessor()
processor.data = [1, 2, 3]
print(list(processor.processor))''',
            "known_issues": [
                {"type": "memory", "severity": "high", "description": "Circular reference prevents garbage collection", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": [1, 2, 3], "expected": [2, 4, 6]}
            ]
        },
        {
            "title": "SQL Injection Vulnerability",
            "description": "This database query is vulnerable to SQL injection.",
            "difficulty": "hard",
            "buggy_code_python": '''def get_user(username):
    """Fetch user from database"""
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    # Imagine this executes on a database
    return query

# Test
print(get_user("admin"))
print(get_user("admin' OR '1'='1"))  # SQL injection!''',
            "known_issues": [
                {"type": "security", "severity": "critical", "description": "Use parameterized queries instead of f-strings", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": "admin", "expected": "SELECT * FROM users WHERE username = 'admin'"}
            ]
        },
        {
            "title": "Race Condition in Counter",
            "description": "This shared counter has a race condition.",
            "difficulty": "hard",
            "buggy_code_python": '''import threading

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
       
        temp = self.count
        temp += 1
        self.count = temp

# Test
counter = Counter()
for _ in range(100):
    counter.increment()
print(counter.count)  # Should be 100''',
            "known_issues": [
                {"type": "concurrency", "severity": "high", "description": "Read-modify-write is not atomic", "line_range": [8, 10]}
            ],
            "test_cases": [
                {"input": 100, "expected": 100}
            ]
        },

        # Add 5 more similar problems to reach 20 total
        {
            "title": "Debug Challenge 16",
            "description": "Find and fix the bug in this sorting algorithm.",
            "difficulty": "medium",
            "buggy_code_python": '''def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([5, 2, 8, 1]))''',
            "known_issues": [
                {"type": "efficiency", "severity": "medium", "description": "Inner loop doesn't account for sorted elements", "line_range": [4, 4]}
            ],
            "test_cases": [
                {"input": [5, 2, 8, 1], "expected": [1, 2, 5, 8]}
            ]
        },
        {
            "title": "Debug Challenge 17",
            "description": "This function removes duplicates but loses order.",
            "difficulty": "easy",
            "buggy_code_python": '''def remove_duplicates(arr):
    return list(set(arr))  

print(remove_duplicates([3, 1, 2, 1, 3, 4]))''',
            "known_issues": [
                {"type": "logic", "severity": "medium", "description": "Using set() loses original order", "line_range": [2, 2]}
            ],
            "test_cases": [
                {"input": [3, 1, 2, 1, 3, 4], "expected": [3, 1, 2, 4]}
            ]
        },
        {
            "title": "Debug Challenge 18",
            "description": "Matrix multiplication has wrong dimensions.",
            "difficulty": "medium",
            "buggy_code_python": '''def matrix_multiply(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(B)):  
            row.append(sum(A[i][k] * B[k][j] for k in range(len(B))))
        result.append(row)
    return result

print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))''',
            "known_issues": [
                {"type": "logic", "severity": "high", "description": "Wrong dimension for columns", "line_range": [5, 5]}
            ],
            "test_cases": [
                {"input": {"A": [[1, 2], [3, 4]], "B": [[5, 6], [7, 8]]}, "expected": [[19, 22], [43, 50]]}
            ]
        },
        {
            "title": "Debug Challenge 19",
            "description": "This linked list reversal has a memory leak.",
            "difficulty": "hard",
            "buggy_code_python": '''class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        
    return prev

# Test with simple case
node1 = Node(1)
node2 = Node(2)
node1.next = node2
print(reverse_list(node1))''',
            "known_issues": [
                {"type": "logic", "severity": "critical", "description": "Infinite loop - forgot current = next_node", "line_range": [13, 13]}
            ],
            "test_cases": [
                {"input": [1, 2, 3], "expected": [3, 2, 1]}
            ]
        },
        {
            "title": "Debug Challenge 20",
            "description": "Password validator has weak security.",
            "difficulty": "medium",
            "buggy_code_python": '''def is_strong_password(password):

    if len(password) >= 6:  
        return True
    return False

print(is_strong_password("abc123"))  # Should be False''',
            "known_issues": [
                {"type": "security", "severity": "high", "description": "Needs length >= 8, uppercase, lowercase, digits", "line_range": [3, 4]}
            ],
            "test_cases": [
                {"input": "abc123", "expected": False},
                {"input": "Abc12345", "expected": True}
            ]
        }
    ]
    
    for p in problems:
        db.add(models.AuditProblem(**p))
    db.commit()
    print(f"Seeded {len(problems)} audit problems")

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