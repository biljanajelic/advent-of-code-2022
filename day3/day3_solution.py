from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters
import itertools

with open ('day3_input.txt') as file:
    data = file.read().split("\n")
    
    
totalsum=0

for i in data:
    half = len(i)//2
    
    left = set (i[:half])
    right = set (i[half:])
    
    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            totalsum += priority+1
            print(char)
            
