items = []
elves = {1:[]}
calories = []
elf_num = 1

with open("advent_day1/cal_input.txt", "r") as input:
    for line in input:
        line = line.strip()
        if line != '':
            # print(elves[elf_num])
            # print(elf_num)
            elves[elf_num].append(int(line))
        else:
            elf_num += 1
            elves[elf_num] = []

# print(elves)
#
        
sums = [sum(calories) for elf, calories in elves.items()]

# print(sums)
print(max(sums))

sums_sorted = sorted(sums, reverse=True)
print(sum(sums_sorted[:3]))