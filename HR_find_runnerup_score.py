#!/usr/bin/python3

#To make the script run by default in python3, either invoke it as python3 script.py or set the shebang line. You can use #!/usr/bin/env python3 for portability across different systems in case they have the language interpreter installed in different locations. That's called a hash-bang.


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    
#    First solution provides an error when total number of elements are more than n. Also does not work when there are more than n numbers of winners
#    top = max(arr)
    
#    for i in range (0,n):
#    	if top == max(arr):
#    		arr.remove(max(arr))
    		
#    print(max(arr))

    x = max(arr)
    y = -999999

    for i in range(0,n):
        if arr[i]<x and arr[i] > y:
            y = arr[i]

    print(y)


