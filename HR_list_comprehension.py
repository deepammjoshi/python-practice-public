#!/usr/bin/python3

#To make the script run by default in python3, either invoke it as python3 script.py or set the shebang line. You can use #!/usr/bin/env python3 for portability across different systems in case they have the language interpreter installed in different locations. That's called a hash-bang.


# you are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to n. 
# Here, 0<=i<=x , 0<=j<=y , 0<=k<=z
# Please use list comprehensions rather than multiple loops, as a learning


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])
    
