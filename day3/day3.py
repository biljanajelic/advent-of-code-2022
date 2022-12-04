from string import ascii_lowercase
from string import ascii_uppercase
from string import ascii_letters

import itertools
import statistics
from statistics import mode

with open ('day3_input.txt') as file:
    data = file.read().split("\n")
  
#print (data)
match=[]

for line in data:
    half = len(line)//2  #find half
    
    left = set (line[:half])  # left half, distinct letters
    right = set (line[half:]) # right half, distinct letters
    
    for i in left:
        if i in right :
            match.append(i)
            #print (match)

def alphabet_position_lower(letter):
    nums = [str(ord(x) - 96) for x in letter.lower() if x >= 'a' and x <= 'z']
    match_letter_sum.append(nums)
    return " ".join(nums)

def alphabet_position_upper(letter):
    nums = [str(ord(x) - 64 + 26) for x in letter.upper() if x >= 'A' and x <= 'Z']
    match_letter_sum.append(nums)
    return " ".join(nums)

listToStr = ' '.join([str(elem) for elem in match]) #convert list into string so we can pass it to the function

#print(alphabet_position(listToStr))
#print(alphabet_position_upper('P'))

match_letter_sum=[]

for i in listToStr:
    if i.isupper():
        alphabet_position_upper(i)
    else:
        alphabet_position_lower(i)
        
#print (match_letter_sum) 

def flatten(l):
    flatList = []
    for elem in l:
        # if an element of a list is a list
        # iterate over this list and add elements to flatList 
        if type(elem) == list:
            for e in elem:
                flatList.append(e)
        else:
            flatList.append(elem)
    return flatList

total=0

for ele in flatten(match_letter_sum):
    total   += int(ele)
    
# printing total value
print("Part 1 answer: ", total)



#Part2

#create a group. first three lines is one group
j=3
total=0

for i in range (0, len(data),3):
    rucksacs = data [i:j]
    j+=3
    for priority, char in enumerate(ascii_letters):
        if char in rucksacs[0] and char in rucksacs[1] and char in rucksacs[2]:
            total +=priority+1
        
print("Part 2 answer: ", total)
