file=open("06 input.txt")
coords=[]
line=file.readline()
while line!="":
    coords.append([int(line.split(",")[0]),int(line.split(",")[1])])
    line=file.readline().replace("\n","")


#grid=[(100000,0)for x in range(0,400) for y in range(0,400)]
grid=[]
for x in range(0,400):
    temp=[]
    for y in range(0,400):
        temp.append([100000,0])
    grid.append(temp)
index=0


for c in coords:
    for x in range(0,400):
        for y in range(0,400):
            dis=(((c[0]-x)**2)**0.5)+(((c[1]-y)**2)**0.5)
            if grid[x][y][0]>dis:
                grid[x][y][0]=dis
                grid[x][y][1]=index

    index+=1

counts=[[0,False] for x in range(0,len(coords))]
print(counts)
for x in range(0,400):
    for y in range(0,400):
        counts[grid[x][y][1]][0]+=1
        if x==0 or x==399 or y==0 or y==399:
            counts[grid[x][y][1]][1]=True
for c in counts:
    if c[1]==False:
        print(c)