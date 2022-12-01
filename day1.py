with open ('day1_input.txt') as file:
    data = file.read().split("\n")

#print (data)

count = 0           # to keep count of the calories
max_count =0        # find max calories

elf_list = []
elf_list_in_list = []
total_calories_per_elf=[]

for i in data:  
    if i=='':       # we want to stop when we see a new row
        count=0
        elf_list_in_list.append(elf_list)
        elf_list=[]
        
    else:
        num=int(i)  # number (int) version of the string in the list

        count += num
          
        elf_list.append(num)  #make a list of all elf totals and then sort the list to take top3 
        #print (elf_list)
        if count > max_count:
            max_count = count         
                               
print ('Part 1 answer:', max_count) # 67450

#print(elf_list_2) # sorted list ascending

#this sums up the calories each elf is carrying
for elf in elf_list_in_list:
    elf_sum = sum(elf)
    total_calories_per_elf.append(elf_sum)

#print(total_calories_per_elf)
total_calories_per_elf.sort() # sorted list ascending
#print(total_calories_per_elf)
print('Part 2 answer:', sum(total_calories_per_elf[-3:]))  #sum the top3 

