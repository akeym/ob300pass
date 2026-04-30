#!/usr/bin/env python3

# these chars align with <space> at 0x20 in ASCII table
lower_start = ['B', '#', '0', 'A', 'I', 'G', '#', '4']
# these chars align with A at 0x41 in ASCII table
upper_start = ['1', 'D', 'Q', '0', '8', '6', 'D', 'U']

lookuptable = ' !#$%&\'()*+,-./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

p = {}
for c in range(1,9):
    p[c] = []
    for x in range(0,33):
        p[c].append(lookuptable[lookuptable.find(lower_start[c - 1]) + x])

for c in range(1,9):
    for x in range(0,62):
        p[c].append(lookuptable[lookuptable.find(upper_start[c - 1]) + x])

print('hex\tchr\t1\t2\t3\t4\t5\t6\t7\t8')
for a in range(0,len(p[1])):
    curr_char = a + 32
    print(f"{curr_char:X}\t{chr(curr_char)}\t{p[1][a]}\t{p[2][a]}\t{p[3][a]}\t{p[4][a]}\t{p[5][a]}\t{p[6][a]}\t{p[7][a]}\t{p[8][a]}")

