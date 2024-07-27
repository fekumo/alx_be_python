#!/usr/bin/env python3


size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:
  
    for _ in range(size):
        print("*", end="")
    
    print()
    # Increment the row counter
    row += 1

