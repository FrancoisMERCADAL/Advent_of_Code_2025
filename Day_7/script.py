FILE_NAME = "input.txt"

def open_parse_file(file):
    lines = []
    nb_line = 0
    for line in file:
        line = list(line.strip())
        if "S" in line:
            start = (nb_line,line.index("S"))
        lines.append(line)
        nb_line += 1
    return lines, start

def calculate_nb_splits(file):
    lines, start = open_parse_file(file)

    def beam_split(lines, start, visited_spots):
        if start[0] == len(lines) - 1:
            return 0
        else:
            left_score = 0
            right_score = 0
            if lines[start[0]+1][start[1]] == "." and (start[0]+1,start[1]) not in visited_spots:
                visited_spots.append((start[0]+1,start[1]))
                return beam_split(lines, (start[0]+1, start[1]), visited_spots)
            elif lines[start[0]+1][start[1]] == "." and (start[0]+1,start[1]) in visited_spots:
                return 0
            
            if lines[start[0]+1][start[1]] == "^":
                if (start[0]+1,start[1]-1) not in visited_spots:
                    visited_spots.append((start[0]+1,start[1]-1))
                    left_score = beam_split(lines, (start[0]+1, start[1]-1), visited_spots)
                if (start[0]+1,start[1]+1) not in visited_spots:
                    visited_spots.append((start[0]+1,start[1]+1))
                    right_score = beam_split(lines, (start[0]+1, start[1]+1), visited_spots)
                return 1 + left_score + right_score

    return beam_split(lines, start, [])

def laboratories_part1():
    file = open(FILE_NAME, "r")
    nb_splits = calculate_nb_splits(file)
    file.close()
    return nb_splits

def calculate_nb_timelines(file):
    lines, start = open_parse_file(file)
    def v2(lines, start, cache):
        if start in cache:
            return cache[start]

        if start[0] == len(lines) - 1:
            return 1
        else:
            left_score = 0
            right_score = 0
            if lines[start[0]+1][start[1]] == ".":
                res = v2(lines, (start[0]+1, start[1]), cache)
                cache[start] = res
                return res

            if lines[start[0]+1][start[1]] == "^":
                left_score = v2(lines, (start[0]+1, start[1]-1), cache)
                right_score = v2(lines, (start[0]+1, start[1]+1), cache)
                cache[start] = left_score + right_score
                return left_score + right_score

    return v2(lines, start, {})

def laboratories_part2():
    file = open(FILE_NAME, "r")
    nb_timelines = calculate_nb_timelines(file)
    file.close()
    return nb_timelines

### TEST AREA
# PART 1
# print(laboratories_part1())
# Output: 1524

# PART 2
print(laboratories_part2())
# Output: 32982105837605
