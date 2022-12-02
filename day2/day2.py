with open ('day2_input.txt') as file:
    data = file.read().split("\n")
  
 #print (data)
 
 # Part 1 Strategy
 # A for Rock, B for Paper, and C for Scissors
 # X for Rock, Y for Paper, and Z for Scissors
 # The score for a single round is the score for the shape you selected
     #(1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round
     #(0 if you lost, 3 if the round was a draw, and 6 if you won).
 
strategy_pt1 = {
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6,
}                               # create a dictionaty of possbile combinations and scores

total_score_pt1=0

for i in data:
    if i in strategy_pt1:   # to handle KeyError 
        total_score_pt1+=strategy_pt1[i]
        #print(total_score)
        
print ('Answer part1:', total_score_pt1)        

# Part 2 strategy:
# X means you need to lose
# Y means draw
# Z means you need to win

strategy_pt2 = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7,
}    
        
total_score_pt2=0

for i in data:
    if i in strategy_pt2:   # to handle KeyError 
        total_score_pt2+=strategy_pt2[i]
        
print ('Answer part2:', total_score_pt2)        

        