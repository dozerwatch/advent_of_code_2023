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
    
def find_let(left_or_right, line):
    '''
    left_or_right:  0 or 1, meaning we are looking
                    for the leftmost or rightmost num respectively
    
    line:           the line we are working on

    return:         the tuple (index in line, left or right most letter) 
                    or (1000000, -1) or (-1,-1) if none 
                    the letter is converted to int
    '''
    
    let = -1

    # Find rightmost letter
    if (left_or_right):
        pos = -1
        # Find the letter with the greatest index
        for letter in valid_letter_digits:
            p = line.rfind(letter)
            if (p == -1):
                continue
            elif (p >= pos):
                pos = p
                let = valid_letter_digits.index(letter) + 1
        return (pos, let)

    # Find leftmost letter
    else:
        pos = 1000000
        # Find the letter with the smallest index
        for letter in valid_letter_digits:
            p = line.find(letter)
            if (p == -1):
                continue
            elif (p <= pos):
                pos = p
                let = valid_letter_digits.index(letter) + 1
        return (pos, let)

with open("./day1/day1_part2_inputs.txt") as f:
    lines = f.read().splitlines()

    lp, ln = 0, 0       # Leftmost position and num
    rp, rn = 0, 0       # Rightmost position and num

    for line in lines:
        lnp, lnn = find_num(0, line)       # Leftmost num position and num
        rnp, rnn = find_num(1, line)       # Rightmost num position and num
        llp, lln = find_let(0, line)       # Leftmost let position and let
        rlp, rln = find_let(1, line)       # Rightmost let position and let

        # Leftmost invalid entries (-1, -1) or (1000000, -1)
        if (lnn == -1):             # num is invalid
            digits += str(lln)
        elif (lln == -1):           # let is invalid
            digits += str(lnn)
        elif (lnp <= llp):          # Get leftmost position and digit
            digits += str(lnn)      # num
        else:                       
            digits += str(lln)      # let

        # Rightmost invalid entries (-1, -1)
        if (rnn == -1):             # num is invalid
            digits += str(rln)
        elif (rln == -1):           # let is invalid
            digits += str(rnn)
        elif (rnp >= rlp):          # Get rightmost position and digit
            digits += str(rnn)      # num
        else:
            digits += str(rln)      # let

        # Both num and let are invalid
        if (lnn == -1 and lln == -1):
            digits = 0

        sum += int(digits)
        print(digits)
        digits = ''

print(sum)
