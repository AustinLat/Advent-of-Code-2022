
with open("input.txt", "r") as r:
    data = r.read().splitlines()

def calorieCounterTopThree(data):
    result = []
    sublist = []
    for line in data:
        if not line.strip():
            if sublist:
                result.append(sublist)
            sublist = []
        else:
            sublist.append(line)

    if sublist:
        result.append(sublist)

    total = 0
    for line in result:
        line = list(map(int, line))
        subtotal = sum(line)
        if subtotal > total:
            total = subtotal
    print(total)


calorieCounterTopThree(data)

