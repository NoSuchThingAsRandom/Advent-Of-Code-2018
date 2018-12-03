#Creates empty canvas
grid = [x[:] for x in [[0] * 1000] * 1000]
file = open("03 input.txt")
claims=file.readlines()
#For each inch on canvas, count number of claims
for c in claims:
    claim=c.split(" ")
    pointer=claim[2].replace(":","").split(",")
    target=claim[3].split("x")
    for x in range(0,int(target[0])):
        for y in range(0,int(target[1])):
            grid[int(pointer[0])+x][int(pointer[1])+y]+=1
#Count number of inches with more than one claim
count=0
for x in grid:
    for y in x:
        if y>1:
            count+=1
print(count)

#Check each claim if each inch has only one claim
for c in claims:
    claim=c.split(" ")
    pointer=claim[2].replace(":","").split(",")
    target=claim[3].split("x")
    possible=True
    for x in range(0,int(target[0])):
        for y in range(0,int(target[1])):
            if grid[int(pointer[0])+x][int(pointer[1])+y]!=1:
                possible=False
    if possible:
        print(claim[0])
        break

