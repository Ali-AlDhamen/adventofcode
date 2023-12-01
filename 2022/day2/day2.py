scores= {
    ("A" , "X") : 4, # draw (3+1)
    ("A" , "Y") : 8, # win ( 6+2)
    ("A" , "Z") : 3, # lose (0+3)
    ("B" , "X") : 1, # lose (0+1)
    ("B" , "Y") : 5, # draw (3+2)
    ("B" , "Z") : 9, # win (6+3)
    ("C" , "X") : 7, # win(6+1)
    ("C" , "Y") : 2, # lose (0+2)
    ("C" , "Z") : 6, # draw (3+3)
}

scores_part2 = {
    ("A" , "X") : 3, # lose (0+3)
    ("A" , "Y") : 4, # draw (3+1)
    ("A" , "Z") : 8, # win (6+2)
    ("B" , "X") : 1, # lose (0+1)
    ("B" , "Y") : 5, # draw (3+2)
    ("B" , "Z") : 9, # win (6+3)
    ("C" , "X") : 2, # lose (0+2)
    ("C" , "Y") : 6, # draw (3+6)
    ("C" , "Z") : 7, # win (6+1)
}


# A, X = Rock 1 | B,Y = Paper 2 | C,Z = Scissors 3
total_points = 0
total_points_part2 = 0
with open('day2/day2.txt') as f:
    for line in f:
        line = line.strip()
        words = line.split()
        total_points += scores[(words[0] , words[1])]
        total_points_part2 += scores_part2[(words[0] , words[1])]


print(total_points)  
print(total_points_part2)
