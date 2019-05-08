# encoding=utf-8
poem = '''\
Programming is fun
When the work is done
If you wanna make your work also fun
    Use Python!
'''

# Open file for 'w'riting
f = open('poem.txt', 'w')

# Write text into file
f.write(poem)

# Close the file
f.close()

# If no mode is specified
# The 'r'ead mode is assumed by default
f = open('poem.txt')

while True:
    line = f.readline()

    # Zero length indicates EOF
    if len(line) == 0:
        break

    # The `line` already has its newline '\n'
    # at the end of each line
    # since it is read from a file.
    print(line, end='')

# Now, close the file.
f.close()
