# encoding=utf-8
with open('poem.txt', 'rt') as f:
    # while True:
    #     line = f.readline()
    #     if len(line) == 0:
    #         break
    #     print(line, end='')
    for line in f:
        print(line, end='')
