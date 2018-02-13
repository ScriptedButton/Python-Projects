# Reversify

import sys

input = sys.argv[1]

output = sys.argv[2]

file_contents = open(input, 'r').read()

reversed = file_contents[::-1]

open(output, 'w').write(reversed)