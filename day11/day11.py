monkeys = {}
line_count = 1
monkey_number = ''
monkey_items = []
monkey_operation = None
monkey_divisible = ''
monkey_true = 0
monkey_false = 0
with open("day11/day11.txt") as f:
    for line in f:
        line = line.strip()
        if line_count == 1:
            monkey_number = line.split(':')[0]

        elif line_count == 2:
            monkey_items = line.split(':')[1].strip().split(',')
        elif line_count == 3:
            monkey_operation = line.split('=')[1].strip().split(" ")

        elif line_count == 4:
            monkey_divisible = line.split('by')[-1].strip()

        elif line_count == 5:
            monkey_true = line.split('monkey')[-1].strip()

        elif line_count == 6:
            monkey_false = line.split('monkey')[-1].strip()
        else:
            monkeys[monkey_number] = {
                'items': monkey_items,
                'operation': monkey_operation,
                'divisible': monkey_divisible,
                'true': monkey_true,
                'false': monkey_false
            }
            line_count = 0
        line_count += 1


result = [0, 0, 0, 0, 0, 0, 0 ,0]

for round in range(20):
    for monkey , monkey_stuff in monkeys.items():
        for item in monkey_stuff["items"]:
            item = int(item)
            op = monkey_stuff["operation"]
            item_str = " ".join(op).replace("old", "item")
            item = eval(item_str)
            item //= 3
            print(item)
            if item % int(monkey_stuff["divisible"]) == 0:
                monkeys[f"Monkey {int(monkey_stuff['true'])}"]["items"].append(item)
                
            else:
                monkeys[f"Monkey {int(monkey_stuff['false'])}"]["items"].append(item)
        result[int(monkey.split()[1])] += len(monkey_stuff["items"])
        monkey_stuff["items"] = []
        



result.sort()
print(result[-1] * result[-2])

