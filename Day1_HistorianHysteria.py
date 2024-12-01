from functool import reduce
list1 = []
list2 = []
with open('./1_input.txt') as file:
    for line in file:
        print(line)
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

list1.sort()
list2.sort()
tot_sum = 0
tot_sum = reduce(
     lambda acc, pair: acc + (pair[0] - pair[1]) if pair[0] > pair[1] else acc,
     zip(list1,list2),
     0
    )

print(tot_sum)