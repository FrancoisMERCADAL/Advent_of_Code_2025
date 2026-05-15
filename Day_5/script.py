FILE_NAME = "input.txt"

def open_parse_file(file):
    file_p2 = False
    ingredients_ids = []
    ingredients_id_ranges = []
    
    for line in file:
        line = line.strip()
        if line == "":
            file_p2 = True
            continue
        
        if file_p2 == True:
            ingredients_ids.append(int(line))
        else:
            line = line.split("-")
            ingredients_id_ranges.append((int(line[0]),int(line[1])))
    return ingredients_id_ranges, ingredients_ids

def get_nb_fresh_ingredients(file):
    fresh_count = 0
    ingredients_id_ranges, ingredients_ids = open_parse_file(file)
    for id in ingredients_ids:
        for range in ingredients_id_ranges:
            if id >= range[0] and id <= range[1]:
                fresh_count += 1
                break
    return fresh_count

def cafeteria_part1():
    file = open(FILE_NAME, "r")
    fresh_count = get_nb_fresh_ingredients(file)
    file.close()
    return fresh_count

def get_fresh_ids(file):
    range_ids = []
    count_ids = 0
    ingredients_id_ranges = open_parse_file(file)[0]
    ingredients_id_ranges.sort()
    for id_range in ingredients_id_ranges:
        if len(range_ids) == 0:
            range_ids.append([id_range[0], id_range[1]])
        else:
            is_change = False
            # inclusion case -> DO NOTHING
            if id_range[0] >= range_ids[-1][0] and id_range[1] <= range_ids[-1][1]:
                is_change == True
                continue
            # lower band is included and upper band is higher
            if id_range[0] >= range_ids[-1][0] and id_range[0] <= range_ids[-1][1] and id_range[1] > range_ids[-1][1]:
                range_ids[-1][1] = id_range[1]
                is_change = True
            if is_change == False:
                range_ids.append([id_range[0], id_range[1]])

    for range_id in range_ids:
        count_ids += 1 + range_id[1] - range_id[0]
    return count_ids

def cafeteria_part2():
    file = open(FILE_NAME, "r")
    count_ids = get_fresh_ids(file)
    file.close()
    return count_ids

### TEST AREA
# PART 1
# print(cafeteria_part1())
# Output: 513

# PART 2
# print(cafeteria_part2())
# Output: 339668510830757
