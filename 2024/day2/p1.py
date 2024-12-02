def check_is_safe(arr):     
    increasing = arr[0] < arr[1]
    
    for i in range(len(arr)-1):
        if (abs(arr[i] - arr[i+1]) < 1 or abs(arr[i] - arr[i+1]) > 3):
            break
        elif (increasing and arr[i] > arr[i+1]) or (not increasing and arr[i] < arr[i+1]):
            break
    else:
        return True
    return False

with open("in.txt", 'r') as f:
    data = f.read().splitlines()
    safe = 0
    
    for line in data:
        arr = list(map(int, line.split(" ")))
        if check_is_safe(arr):
            safe += 1

    print(safe)