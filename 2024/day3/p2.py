import re
with open("in.txt", 'r') as f:
    data = f.read()
    pattern = r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)"
    matches = re.finditer(pattern, data)
    ans = 0
    counting = True
    for match in matches:
        match_text = match.group()
        if match_text.startswith('don\'t'):
            counting = False
        elif match_text.startswith('do'):
            counting = True
        if counting and match_text.startswith('mul'):
            a, b = match_text.split(',')
            a = a.split('(')[1]
            b = b.split(')')[0]
            ans += int(a) * int(b)
    print(ans)
    