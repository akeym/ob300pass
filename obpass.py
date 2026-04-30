import sys

# Generate a bypass password for an HP Omnibook 300

# these chars align with <space> at 0x20 in ASCII table 
lower_start = ['B', '#', '0', 'A', 'I', 'G', '#', '4']
# these chars align with A at 0x41 in ASCII table
upper_start = ['1', 'D', 'Q', '0', '8', '6', 'D', 'U']

# starts like ascii order, but..
lookuptable = ' !#$%&\'()*+,-./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upper_start_offset = ord('A')

ciphertext = str(sys.argv[1]).upper()
if len(ciphertext) > 8:
    print('Error: Max length is 8 chars')
    sys.exit()

for x in range(0, len(ciphertext)):
    # only digits are valid results in ASCII 0x20 thru 0x40 inclusive
    start_pos = lookuptable.find(lower_start[x])
    table = lookuptable[start_pos:]
    offset = table.find(ciphertext[x])
    password_char = chr(offset + ord(' '))
    if ord(password_char) >= ord('0') and ord(password_char) <= ord('9'):
        print(password_char, end='')
    else:
        # didn't match a number char, upper list.
        start_pos = lookuptable.find(upper_start[x])
        table = lookuptable[start_pos:]
        offset = table.find(ciphertext[x])
        print(chr(upper_start_offset + offset),end='')
print('')


