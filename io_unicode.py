# encoding=utf-8
import io

f = open('abc.txt', 'wt', encoding='utf-8')
# Coding under python v.2~ using the unicode type `u`
# f.write(u'Imagine here are some non-English characters, eg. 你好！')
# Coding under python v.3~
f.write('Imagine here are some non-English characters, eg. 你好！')
f.close()

txt = io.open('abc.txt', encoding='utf-8').read()
print(txt)
