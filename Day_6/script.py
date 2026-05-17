FILE_NAME = "input.txt"

def calculate_result_p1(file):
    parsed_lines = []
    index_symbols = 0

    for line in file:
        line = line.strip().split(" ")
        line = [x for x in line if x != ""]
        if line[0].isnumeric():
            parsed_lines.append([int(x) for x in line])
            index_symbols += 1
        else:
            parsed_lines.append([x for x in line])

    result = 0
    for i in range(len(parsed_lines[0])):
        if parsed_lines[index_symbols][i] == "*":
            calculation = 1
            for k in range(index_symbols):
                calculation *= parsed_lines[k][i]
        elif parsed_lines[index_symbols][i] == "+":
            calculation = 0
            for k in range(index_symbols):
                calculation += parsed_lines[k][i]
        result += calculation

    return result

def trash_compactor_part1():
    file = open(FILE_NAME, "r")
    result = calculate_result_p1(file)
    file.close()
    return result

def calculate_result_p2(file):
    parsed_lines = []
    for line in file:
        line = [x for x in line if x != ""]
        if len(parsed_lines) == 0:
            for k in range(len(line)):
                parsed_lines.append([line[k]])
        else:
            for k in range(len(line)):
                parsed_lines[k].append(line[k])

    symbols = []
    for i in range(len(parsed_lines)-1):
        parsed_lines[i] = [x for x in parsed_lines[i] if x != " "]
        parsed_lines[i] = "".join(parsed_lines[i])

        if len(parsed_lines[i]) > 0 and (parsed_lines[i][-1] == "+" or parsed_lines[i][-1] == "*"):
            symbols.append(parsed_lines[i][-1])
            parsed_lines[i] = parsed_lines[i][:-1]

    parsed_lines = parsed_lines[:-1]
    parsed_lines = [int(x) if x != "" else "" for x in parsed_lines]

    index_symbol = 0
    pre_results = [0 if x == "+" else 1 for x in symbols]
    for nb in parsed_lines:
        if nb != "":
            if symbols[index_symbol] == "+":
                pre_results[index_symbol] += nb
            else:
                pre_results[index_symbol] *= nb
        else:
            index_symbol += 1
    return sum(pre_results)

def trash_compactor_part2():
    file = open(FILE_NAME, "r")
    result = calculate_result_p2(file)
    file.close()
    return result

### TEST AREA
# PART 1
# print(trash_compactor_part1())
# Output: 4648618073226

# PART 2
# print(trash_compactor_part2())
# Output: 7329921182115
