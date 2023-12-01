import string


calories  = {}
count = 1
sum_calories = 0

with open('day1/day1.txt') as f:
    for line in f:
        if line != "\n":
            sum_calories += int(line.strip(string.ascii_letters))
        else:
            calories[count] = sum_calories
            count += 1
            sum_calories = 0

highest_calories = max(calories.values())

calories_values  = sorted(calories.values())
top_three = sum(calories_values[-3:])
print(f"top calories {highest_calories}")
print(f"top three calories {top_three}")