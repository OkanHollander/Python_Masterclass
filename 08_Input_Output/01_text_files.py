# jabber = open('Jabberwocky.txt','r')

# for line in jabber:
#     print(line, end='')

# jabber.close()
with open('Jabberwocky.txt','r') as f:
    # for line in f:
    #     print(line, end='')
#     lines = f.readlines()

# print(lines, end='')
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end='')
    text = f.read()
print(text)

with open('Jabberwocky.txt') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if 'jubjub' in line.casefold():
            break