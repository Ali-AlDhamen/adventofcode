digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}
with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    ans = 0
    for line in data:
        temp = []
        st = ""
        for ch in line:
            if ch.isnumeric():
                temp.append(ch)
            else:
                st += ch
                found = ""
                for digit in digits:
                    if digit in st:
                        found = digit
                        break
                if found != "":
                    temp.append(str(digits[found]))
                    st = ch # if i put st = "" then it will be wrong because eightwo is 82 not 8wo
        ans += int(temp[0] + temp[-1])
    print(ans)
