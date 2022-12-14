total = 0

with open("advent_of_code_2022/advent_day4/assignments.txt", "r") as file:
    for line in file:
        contents = line.split(",")
        elf1 = contents[0]
        elf2 = contents[1]
        elf1_start, elf1_stop = elf1.split("-")[0], elf1.split("-")[1]
        elf2_start, elf2_stop = elf2.split("-")[0], elf2.split("-")[1]
        elf1_range = range(int(elf1_start), int(elf1_stop) + 1)
        elf2_range = range(int(elf2_start), int(elf2_stop) + 1)

        counter = 0

        for item in range(int(elf1_start), int(elf1_stop) + 1):
            if item in range(int(elf2_start), int(elf2_stop) + 1):
                total += 1
                break

print(total)