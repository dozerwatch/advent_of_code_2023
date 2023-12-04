# Check if character s is an int
# Return the type
def check_int(s):
    try:
        return type(int(s))
    except ValueError:
        return type(s)

sum = 0
digits = ''

with open("day1_part1_inputs.txt", 'r') as f:
    lines = f.readlines()
    
    for line in lines:

        # Check left to right
        for char in line:
            t = check_int(char)
            if t == int:
                digits += char
                break

        # Check right to left
        for char in line[::-1]:
            t = check_int(char)
            if t == int:
                digits += char
                break

        digits = int(digits)
        sum += digits
        digits = ''

print(sum)