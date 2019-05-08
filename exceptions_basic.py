# encoding=utf-8
try:
    text = input('Plz enter something:')
except EOFError:
    print('\nThis is a EOFError')
except KeyboardInterrupt:
    print('\nThis is a KeyboardInterrupt')
else:
    print('Your input is', text)
