from math import gcd

with open("in.txt", "r") as f:

    steps = f.readline().strip()
    f.readline()
    data = f.read().splitlines()
    
    nodes_map = {}
    steps_count = 0
    current_node = 'AAA'
    for i, line in enumerate(data):
        data[i] = line.split(" ")
        nodes_map[data[i][0]] = (data[i][2][1:-1], data[i][3][:-1])

    positions = [key for key in nodes_map if key[-1] == "A"]
    cycles = []

    for current in positions:
        cycle = []

        current_steps = steps
        step_count = 0
        first_z = None

        while True:
            while step_count == 0 or not current[-1] == "Z":
                step_count += 1
                current = nodes_map[current][0 if current_steps[0] == "L" else 1]
                current_steps = current_steps[1:] + current_steps[0]

            cycle.append(step_count)

            if first_z is None:
                first_z = current
                step_count = 0
            elif current == first_z:
                break

        cycles.append(cycle)

    nums = [cycle[0] for cycle in cycles]

    lcm = nums.pop()

    for num in nums:
        lcm = lcm * num // gcd(lcm, num)

    print(lcm)