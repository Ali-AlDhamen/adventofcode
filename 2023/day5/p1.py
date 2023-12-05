with open("in.txt", 'r') as f:
    seeds = list(map(int, f.readline().strip().split(" ")[1:]))
    data = [line.strip() for line in f.readlines() if line.strip()]
    exchange = {}
    
    for i, line in enumerate(data):
        if not line[0].isdigit():
            if exchange:
                seeds = [exchange.get(seed, seed) for seed in seeds]
                exchange = {}
            continue  
        
        values = list(map(int, data[i].split(" ")))
        des_start = values[0]
        source_start = values[1]
        length = values[2]  
        for add in range(length):
            if source_start+add not in exchange:
                exchange[source_start+add] = des_start+add
    seeds = [exchange.get(seed, seed) for seed in seeds]
    print(min(seeds))