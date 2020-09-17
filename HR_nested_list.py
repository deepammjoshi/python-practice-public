#!/usr/bin/python3

#To make the script run by default in python3, either invoke it as python3 script.py or set the shebang line. You can use #!/usr/bin/env python3 for portability across different systems in case they have the language interpreter installed in different locations. That's called a hash-bang.

#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of #any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name #on a new line.

if __name__ == '__main__':
 #for _ in range(int(input())):
    
    score = float(input())
    name = input()
    marksheet = []
    for _ in range(int(input())):
        marksheet.append([name, score])

    second_highest = sorted(list(set([score for name, score in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))  	
