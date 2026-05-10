FILE_NAME = "input.txt"

def get_joltage(file):
    jolt_sum = 0
    file = open(FILE_NAME, "r")
    for line in file:
        line = list(line.strip())
        nb_1, nb_2 = line[0], line[1]
        for i in range(2, len(line)):
            new_nb = max(int(nb_1 + line[i]),int(nb_2 + line[i]))
            if new_nb > int(nb_1 + nb_2):
                new_nb = list(str(new_nb))
                nb_1, nb_2 = new_nb[0], new_nb[1]
        jolt_sum += int(nb_1 + nb_2)
    return jolt_sum

def lobby_part1():
    file = open(FILE_NAME, "r")
    joltage = get_joltage(file)
    file.close()
    return joltage

def get_joltage2(file):
    total_sum = 0
    battery_size = 12
    
    for line in file:
        line = [int(x) for x in list(line.strip())]
        to_remove = len(line) - battery_size
        stack = []

        for nb in line:
            while to_remove > 0 and stack and stack[-1] < nb:
                stack.pop()
                to_remove -= 1
            stack.append(nb)
        
        result = int("".join(map(str, stack[:battery_size])))
        total_sum += result

    return total_sum

def lobby_part2():
    file = open(FILE_NAME, "r")
    joltage = get_joltage2(file)
    file.close()
    return joltage

### TEST AREA
# PART 1
# print(lobby_part1())
# Output: 17095

# PART 2
# print(lobby_part2())
# Output: 168794698570517
