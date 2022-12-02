
with open("input.txt", "r") as r:
    data = r.read().splitlines()

def calorieCounter(input):
    count_list = []
    count = 0
    temp_total = 0
    while count < len(input):
        if input[count] != "":
            temp_total += int(input[count])
            count += 1
            if count == len(input):
                count_list.append(temp_total)
                break
        else:
            count_list.append(temp_total)
            temp_total = 0
            count += 1

    return count_list
        
def calorieCounterTopThree(data):
    count_list = calorieCounter(data)
    topTotal = 0
    for i in range(3):
        lastIndex = count_list.index(max(count_list))
        largest_value = count_list.pop(lastIndex)
        topTotal += largest_value
    print(topTotal)


calorieCounterTopThree(data)

