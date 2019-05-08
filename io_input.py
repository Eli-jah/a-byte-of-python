# encoding=utf-8
import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


regex = re.compile(r'[,.:?!]')
something = input('Plz input something:').strip(' ').lower()
string = regex.sub('', something)
# Filtered by the regular expression,
# "Rise to vote, sir." is also a palindrome.
if is_palindrome(string):
    print('This is a palindrome: {}'.format(string))
else:
    print('This is not a palindrome: {}'.format(string))
