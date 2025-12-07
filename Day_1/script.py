FILE_NAME = "instructions.txt"

# PART 1
def make_rotation(current_val, direction, val):
    if direction == "R":
        current_val += val
        while current_val >= 100:
            current_val -= 100
    elif direction == "L":
        current_val -= val
        while current_val < 0:
            current_val += 100
    return current_val

def get_nb_0(file):
    current_val = 50
    count_0 = 0
    for line in file:
        line = (line.strip())
        direction, val = line[0], int(line[1:])
        current_val = make_rotation(current_val, direction, val)
        if current_val == 0:
            count_0 += 1
    return count_0

def secret_entrance_part1():
    file = open(FILE_NAME, "r")
    count_0 = get_nb_0(file)
    file.close()
    return count_0

# PART 2
def make_rotation_p2(current_val, direction, val):
    hit_0 = int(val/100)
    val = val % 100

    if direction == "R":
        current_val += val
        if current_val >= 100:
            hit_0 += int(current_val/100)
            current_val = current_val % 100
    elif direction == "L":
        if current_val == 0:
            hit_0 -= 1
        current_val -= val
        if current_val <= 0:
            hit_0 += int(current_val/100) + 1
            current_val = current_val % 100
    return current_val, hit_0

def get_hit_0(file):
    current_val = 50
    count_0 = 0
    hit_0 = 0
    for line in file:
        line = (line.strip())
        direction, val = line[0], int(line[1:])
        current_val, hit_0 = make_rotation_p2(current_val, direction, val)
        count_0 += hit_0
    return count_0

def secret_entrance_part2():
    file = open(FILE_NAME, "r")
    hit_0 = get_hit_0(file)
    file.close()
    return hit_0

### TEST AREA
# PART 1
# print(secret_entrance_part1())
# Output: 1097

# PART 2
# print(secret_entrance_part2())
# Output: 7101
