# encoding=utf-8
class ShortInputException(Exception):
    """A user-defined exception class."""

    def __init__(self, length, at_least):
        Exception.__init__(self)
        self.length = length
        self.at_least = at_least


try:
    text = input('Plz input something:')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    # Other work could go on here
    # ...
except EOFError:
    print('\nThis is a EOFError')
except KeyboardInterrupt:
    print('\nThis is a KeyboardInterrupt')
except ShortInputException as sie:
    print('ShortInputException: Your input consists only {} characters, and it is too short, plz enter at least {} characters.'.format(sie.length, sie.at_least))
else:
    print('Your input is', text)
