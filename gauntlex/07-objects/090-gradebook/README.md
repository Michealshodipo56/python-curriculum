# Student Averages

## Description
Collect scores by student and compute an average only when scores exist.

### Behavior contract
Implement Gradebook with add_score(student,score) and average(student). Scores must be 0 through 100 inclusive. Average returns None for students without scores.

## Requirements
- Define `Gradebook` in `starter/solution.py`.
- Implement the documented methods and exception behavior.
- Do not read input or print at import time.
- Use the Python standard library only.

## Tips
Distinguish a student with no scores from a student whose average is zero.

Think through the object's state before and after each operation, including invalid operations. Implement the behavior yourself; no solution code is provided.
