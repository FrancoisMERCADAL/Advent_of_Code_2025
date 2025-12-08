FILE_NAME = "input.txt"

def open_parse_file():
    file = open(FILE_NAME, "r")
    lines = []
    for line in file:
        lines.append(line.strip())
    line = ''.join(lines)
    sets = line.split(',')
    file.close()
    return sets

def gift_shop_part1():
    sets = open_parse_file()
    sum_ids = 0
    for set in sets:
        set = set.split('-')
        lower_bound = int(set[0])
        upper_bound = int(set[1])
        for i in range(lower_bound,upper_bound+1):
            nb_str = str(i)
            if len(nb_str) % 2 == 0 and nb_str[0:int(len(nb_str)/2)] == nb_str[int(len(nb_str)/2):]:
                sum_ids += i
    return sum_ids

def gift_shop_part2():
    sets = open_parse_file()
    sum_ids = 0
    for set in sets:
        set = set.split('-')
        lower_bound = int(set[0])
        upper_bound = int(set[1])
        for nb in range(lower_bound,upper_bound+1):
            nb_str = str(nb)
            for len_chunk in range(1,int(len(nb_str)/2)+1):
                chunk_str = nb_str[0:len_chunk]
                if chunk_str * int(len(nb_str)/len_chunk) == nb_str:
                    sum_ids += int(nb_str)
                    break
    return sum_ids

### TEST AREA
# PART 1
# print(gift_shop_part1())
# Output: 31000881061

# PART 2
# print(gift_shop_part2())
# Output: 46769308485
