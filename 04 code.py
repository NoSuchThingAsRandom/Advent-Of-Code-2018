from datetime import datetime
import time
start=time.time()
file =open("04 input.txt")
data=file.readlines()
sorted=[]
#Sorts file
while len(data)!=0:
    pos=0
    earliest=datetime.strptime(data[0].split("]")[0].replace("[","").replace("-"," ").replace(":"," "),"%Y %m %d %H %M")
    for x in range(0,len(data)):
        if earliest>datetime.strptime(data[x].split("]")[0].replace("[","").replace("-"," ").replace(":"," "),"%Y %m %d %H %M"):
            pos=x
            earliest=datetime.strptime(data[x].split("]")[0].replace("[","").replace("-"," ").replace(":"," "),"%Y %m %d %H %M")
    add=data.pop(pos)
    sorted.append(add)
print("Sorted")
print(time.time()-start)
sleep={}
current_guard=0
#print(sorted[0][15:17])
for s in sorted:
#    print(s) 
    if "Guard" in s:
        temp=s[26:30]
        id=""
        for i in temp:
            try:
                id+=str(int(i))
            except ValueError:
                break
        if int(id) not in sleep:
            sleep[int(id)]=[0]*60
        current_guard=int(id)
    elif "falls asleep" in s:
        for x in range(int(s[15:17]),60):
            sleep[current_guard][x]+=1
    elif "wakes up" in s:
        for x in range(int(s[15:17]),60):
            sleep[current_guard][x]-=1
highest=0
minute=0
guard=0
guard_total={}
high_guard=0
high_total=0
total=0


for g,x in sleep.items():
    temp_min=0
    temp=0
    total=0
    for t in range(0,len(x)):
        if x[t]>=temp:
            temp=x[t]
            temp_min=t
        if x[t]>=highest:
            highest=x[t]
            minute=t
            guard=g
        total+=x[t]
    if total>high_total:
        high_total=total
        high_guard=g
        high_min=temp_min
        

print("Guard: "+str(guard)+" spent "+str(highest) +" times asleep at "+str(minute)) 
print("Guard: "+str(high_guard)+" spent the most time asleep: "+str(high_total)+" with a common minute of : "+str(high_min)) 
