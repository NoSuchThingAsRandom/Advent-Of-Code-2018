def fuck(polymer):
    repeat=False
    index=0
    #print(num)
    while index<len(polymer)-1:
        if polymer[index].lower()==polymer[index+1].lower():
            if polymer[index].isupper() and polymer[index+1].islower():
               polymer=polymer[:index]+polymer[index+2:]
               index=index-2
               repeat=True
               if index<0:
                index=0
            elif polymer[index+1].isupper() and polymer[index].islower():
                polymer=polymer[:index]+polymer[index+2:]
                repeat=True
                index=index-2
                if index<0:
                    index=0
        index+=1
        #print("     "+str(index))
    #num+=1
    if repeat:
        return fuck(polymer)
    return polymer

file=open("05 input.txt")
polymer=file.read()
#Remove all instances of polymer
letter="a"
result={}
for x in range(0,26):
    polymerCurrent=polymer
    polymerCurrent=polymerCurrent.replace((str(chr(ord(letter)+x))),"")
    polymerCurrent=polymerCurrent.replace((str(chr(ord(letter)+x)).upper()),"")
    #React
    result[chr(ord(letter)+x)]=len(fuck(polymerCurrent))


print(result)
smallest=result[chr(ord(letter))]
le=""
for x in range(0,26):
    if result[chr(ord(letter)+x)]<smallest:
        smallest=result[chr(ord(letter)+x)]
        le=str(chr(ord(letter)+x))
print("The smallest is " +le +" with a length of "+str(smallest))
print(len(fuck(polymer)))
print(len(fuck(polymer)))
