#!/usr/bin/python3

#To make the script run by default in python3, either invoke it as python3 script.py or set the shebang line. You can use #!/usr/bin/env python3 for portability across different systems in case they have the language interpreter installed in different locations. That's called a hash-bang.

#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Import decimal
from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# Extract the values into a list: query_scores
query_scores = student_marks[query_name]
print(query_scores)
# Sum the scores in the list: total_scores
total_scores = sum(query_scores)
print(total_scores)
# Convert the floats to decimals and average the scores: avg
avg = Decimal(total_scores/3)
print(avg)
# Print the mean of the scores, correct to two decimals
print(round(avg,2))
