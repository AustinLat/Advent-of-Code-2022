
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

    new_list = []

    for line in result:
        line = list(map(int, line))
        subtotal = sum(line)
        new_list.append(subtotal)

         



    top_three = sorted(new_list, reverse=True)[:3]
    print(sum(top_three))



calorieCounterTopThree(data)

