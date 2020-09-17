# Print the list of integers from  through  as a string, without spaces.

#!/usr/bin/python3

if __name__ == '__main__':
    n = int(input())
    print(*range(1,n+1),sep='')
    
# The * is used to unpack a iterable(list, string,tuple etc) in python
# >>> print(*range(0,4))
# 0 1 2 3
# >>> print(*(2,3))
# 2 3
# >>> print(*[0,5,7])
# 0 5 7

# Range gives us numbers between 2 given numbers
# >>> range(0,4)
# [0,1,2,3]
# >>> range(2,5)
# [2,3,4]
# >>> range(3,7)
# [3,4,5,6]


# To remove the space we can use  sep=""
# >>> print(*range(0,4), sep="")
# 0123
# >>> print(*(2,3),sep=",")
# 2,3
# >>> print(*[0,5,7], sep="\n")
# 0
# 5
# 7
