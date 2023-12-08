with open("in.txt" ,"r") as f:
    steps = f.readline().strip()
    f.readline()
    data = f.read().splitlines()
    print(steps)
    
    nodes_map = {}
    steps_count = 0
    current_node = 'AAA'
    for i, line in enumerate(data):
        data[i] = line.split(" ")
        nodes_map[data[i][0]] = (data[i][2][1:-1], data[i][3][:-1])
        
    while current_node != "ZZZ":
        step = steps[steps_count%len(steps)] 
        steps_count += 1
        
        if step == "R":
            next_node = nodes_map[current_node][1]
        else:
            next_node = nodes_map[current_node][0]
        current_node = next_node 
    print(steps_count)
    
    
    