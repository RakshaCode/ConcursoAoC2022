list = []

inElfInventory = False
cont = 0

with open('input.txt','r') as file:
    for line in file:
        line = line.strip('\n')
        if line:
            if inElfInventory:
                list[-1] = int(line) + int(list[-1])
            else:
                list.append(int(line))
                inElfInventory = True
        else:
            inElfInventory = False
list.sort(reverse=True)
print(sum(list[0:3]))