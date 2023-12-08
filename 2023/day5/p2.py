with open("in.txt", 'r') as f:
    inputs, *steps = f.read().split("\n\n")

    inputs = list(map(int, inputs.split(":")[1].split()))

    seeds = []

    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

    for step in steps:
        ranges = []
        for line in step.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))
        new = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for start_dest, start_source, length in ranges:
                overlap_start = max(start, start_source)
                overlap_end = min(end, start_source + length)
                if overlap_start < overlap_end:
                    new.append((overlap_start - start_source + start_dest, overlap_end - start_source + start_dest))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new.append((start, end))
        seeds = new

    print(min(seeds)[0])

