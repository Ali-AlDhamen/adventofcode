with open("in.txt", 'r') as f:
    steps = f.read().strip().split("\n\n")


    seeds = list(map(int, steps.pop(0).split(":")[1].split()))

    
    for step in steps:
        ranges = []
        
        for line in step.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        
        
        new_seeds = []
        for seed in seeds:
            for start_dest, start_source, length in ranges:
                if start_source <= seed < start_source + length:
                    new_seeds.append(seed - start_source + start_dest)
                    break
            else:
                new_seeds.append(seed)
        seeds = new_seeds

    
    print(min(seeds))

    
