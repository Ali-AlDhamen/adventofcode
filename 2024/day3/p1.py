import re
with open("in.txt", 'r') as f:
    data = f.read()
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.finditer(pattern, data)
    ans = 0
    for match in matches:
        a,b  = match.group().split(",")
        a = a.split("(")[1]
        b = b.split(")")[0]
        ans += int(a) * int(b)
    print(ans)
    