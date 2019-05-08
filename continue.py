# encoding=utf-8
while True:
    s = input('Enter something : ')
    if s == 'quit':
        print('quitting ...')
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length: {0}'.format(len(s)))
    # Do other kinds of processing here...
print('Done')
