import re

SYMBOLS = {'=', '/', '+', '#', '*', '$', '@', '-', '%', '&'}
SUM = 0

def find_nums(line_num, line):
    '''
        Find all numbers in given line.
        Return a list of 4-tuples containing 
            1. line number
            2. starting index
            3. length of number
            4. the actual number
    '''
    lst = []
    nums = re.findall(r'\d+', line)         # Find all numbers in line
    for num in nums:
        index = line.index(num)
        length = len(num)
        lst.append((line_num, index, length, num))
    return lst

def is_adjacent_to_symbol(lines, num):
    '''
        lines:
            List containing each line of puzzle input as entries
        
        num:
            A 4-tuples containing 
                1. line number
                2. starting index
                3. length of number
                4. the actual number
        
        Return True if there are symbols adjacent to number, otherwise False.
    '''
    line_num, s, length, _ = num
    e = s+length-1      # Index of last number
    b = len(lines)-1    # Bottom row & last column

    try:
        lines[line_num-1][s-1:e+2] # Top row
    except:
        
        lines
        return any([x in SYMBOLS for x in lines[line_num-1][s-1:e+2]]) or any([x in SYMBOLS for x in lines[line_num+1][s-1:e+2]]) or (lines[line_num][s-1] in SYMBOLS) or (lines[line_num][e+1] in SYMBOLS) 

with open('./day3/part1/test.txt', 'r') as f:
    lines = f.read().splitlines()
    for line_number, line in enumerate(lines):
        list_of_nums = find_nums(line_number, line)
        for num in list_of_nums:
            if is_adjacent_to_symbol(lines, num):
                SUM += int(num[3])

print(SUM)