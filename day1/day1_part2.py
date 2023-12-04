# Check if character s is an int
# Return the type
def check_int(s):
    try:
        return type(int(s))
    except ValueError:
        return type(s)

valid_letter_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Return the left and right most letter digit and their position in string line
def find_letter_digits(line):
    leftmost_pos = 99999999
    leftmost_letter_digit = ''
    rightmost_pos = -1
    rightmost_letter_digit = ''

    for letter_digit in valid_letter_digits:
        
        p = line.find(letter_digit)

        # Find left most valid letter digit
        if p > -1 and p < leftmost_pos:
            leftmost_pos = p
            leftmost_letter_digit = letter_digit

        # Find right most valid letter digit
        if p > rightmost_pos:
            rightmost_pos = p
            rightmost_letter_digit = letter_digit

    return (leftmost_pos,leftmost_letter_digit), (rightmost_pos, rightmost_letter_digit)
            

sum = 0
digits = ''

with open("./day1/test.txt", 'r') as f:
    lines = f.read().splitlines()
    
    for line in lines:

        left, right = find_letter_digits(line)

        # Check left to right
        pos = 0
        for char in line:
            t = check_int(char)
            if t == int:
                if pos < left[0]:
                    digits += char
                else:
                    digits += str(valid_letter_digits.index(left[1]) + 1)
                break
            pos += 1

            # Case where there are no numbers
            if pos == len(line):
                digits += str(valid_letter_digits.index(left[1]) + 1)

        # Check right to left
        pos = len(line)-1
        for char in line[::-1]:
            t = check_int(char)
            if t == int:
                if pos > right[0]:
                    digits += char
                else:
                    digits += str(valid_letter_digits.index(right[1]) + 1)
                break
            pos -= 1

            # Case where there are no numbers
            if pos == -1:
                digits += str(valid_letter_digits.index(right[1]) + 1)
            
        digits = int(digits)
        print(digits)
        sum += digits
        digits = ''

print("Sum: \t", sum)