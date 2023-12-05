valid_letter_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digits = ''
sum = 0

def find_num(left_or_right, line):
    '''
    left_or_right:  0 or 1, meaning we are looking
                    for the leftmost or rightmost num respectively
    
    line:           the line we are working on

    return:         the tuple (index in line, left or right most number) or (-1,-1) if none 
    '''

    pos, num = 0, 0

    # Find rightmost num
    if (left_or_right):
        # Find first num in line
        for c in line[::-1]:
            try:
                num = int(c)
                pos = line.index(c)
                return (pos, num)
            except ValueError:
                pass
        return (-1,-1)
    
    # Find leftmost num
    else:
        # Find first num in line
        for c in line:
            try:
                num = int(c)
                pos = line.index(c)
                return (pos, num)
            except ValueError:
                pass
        return (-1,-1)
    
def find_letter(left_or_right, line):
    '''
    left_or_right:  0 or 1, meaning we are looking
                    for the leftmost or rightmost num respectively
    
    line:           the line we are working on

    return:         the tuple (index in line, left or right most letter) or (-1,-1) if none 
                    the letter is converted to int
    '''
    
    pos, let = 0, 0

    






with open("./day1/test.txt") as f:
    lines = f.read().splitlines()

    for line in lines:
        print(find_num(1, line))