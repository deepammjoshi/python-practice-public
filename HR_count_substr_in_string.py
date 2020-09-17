#!/usr/bin/python3

#To make the script run by default in python3, either invoke it as python3 script.py or set the shebang line. You can use #!/usr/bin/env python3 for portability across different systems in case they have the language interpreter installed in different locations. That's called a hash-bang.

#Count overlapping substring in a given string

def CountOccurrences(string, substring): 
  
    # Initialize count and start to 0 
	count = 0
	start = 0
  
    # Search through the string till 
    # we reach the end of it 
	while start < len(string): 
  
        # Check if a substring is present from 
        # 'start' position till the end 
		pos = string.find(substring, start) 
  
		if pos != -1: 
            # If a substring is present, move 'start' to 
            # the next position from start of the substring 
			start = pos + 1
  
            # Increment the count 
			count += 1
		else: 
            # If no further substring is present 
			break
    # return the value of count 
	return count
    
# Driver Code 
string = "GeeksforGeeksforGeeksforGeeks"
print(CountOccurrences(string, "GeeksforGeeks")) 
