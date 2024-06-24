def reverse_integer(x):
    s = str(x) # this converts an integer into a string
    if s[0] == '-':
        reversed_s = '-' + s[:0:-1] # concatenation of the string
    else:
        reversed_s = s[::-1] # reversing a string
    reversed_x = int(reversed_s)
    return reversed_x
num1 = 123
num2 = -476
print(f"Reversed integer of {num1}: {reverse_integer(num1)}")
print(f"Reversed integer of {num2}: {reverse_integer(num2)}")


