# encoding=utf-8
import sys
import time

f = None
try:
    f = open('poem.txt')
    # Our usual file-reading idiom
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()  # to make sure the output to be printed to the screen immediately
        print('Plz press Ctrl+C Now')
        # To make sure that it runs for a while
        time.sleep(1)
except IOError:
    print('Could not find the file poem.txt')
except KeyboardInterrupt:
    print('You cancelled the file reading')
finally:
    if f:
        f.close()
    print('(Done: file closed)')
