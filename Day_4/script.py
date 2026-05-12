FILE_NAME = "input.txt"

def open_parse_file(file):
    lines = []
    for line in file:
        line = list(line.strip())
        lines.append(line)
    return lines

def get_neighbours(line, col, lines):
    return_arr = []
    # N
    if line - 1 >= 0:
        return_arr.append(lines[line-1][col])
    # NE
    if line - 1 >= 0 and col + 1 < len(lines[line]):
        return_arr.append(lines[line-1][col+1])
    # E
    if col + 1 < len(lines[line]):
        return_arr.append(lines[line][col+1])
    # SE
    if line + 1 < len(lines) and col + 1 < len(lines[line]):
        return_arr.append(lines[line+1][col+1])
    # S
    if line + 1 < len(lines):
        return_arr.append(lines[line+1][col])
    # SW
    if line + 1 < len(lines) and col - 1 >= 0:
        return_arr.append(lines[line+1][col-1])
    # W
    if col - 1 >= 0:
        return_arr.append(lines[line][col-1])
    # NW
    if line - 1 >= 0 and col - 1 >= 0:
        return_arr.append(lines[line-1][col-1])
    return return_arr

def count_paper_rolls(file):
    lines = open_parse_file(file)
    count = 0
    for line in range(len(lines)):
        for col in range(len(lines[line])):
            if lines[line][col] == "@":
                neighbours = get_neighbours(line, col, lines)
                if neighbours.count("@") < 4:
                    count += 1
    return count

def printing_department_part1():
    file = open(FILE_NAME, "r")
    count = count_paper_rolls(file)
    file.close()
    return count

def implement_changes(lines, changes_to_make):
    for tuple in changes_to_make:
        lines[tuple[0]][tuple[1]] = "."
    return lines

def count_paper_rolls_p2(file):
    lines = open_parse_file(file)
    count = 0

    while True:
        changes_to_make = []
        for line in range(len(lines)):
            for col in range(len(lines[line])):
                if lines[line][col] == "@":
                    neighbours = get_neighbours(line, col, lines)
                    if neighbours.count("@") < 4:
                        changes_to_make.append((line,col))
        if len(changes_to_make) == 0:
            break
        count += len(changes_to_make)
        lines = implement_changes(lines, changes_to_make)
    
    return count

def printing_department_part2():
    file = open(FILE_NAME, "r")
    count = count_paper_rolls_p2(file)
    file.close()
    return count

### TEST AREA
# PART 1
# print(printing_department_part1())
# Output: 1549

# PART 2
# print(printing_department_part2())
# Output: 8887
