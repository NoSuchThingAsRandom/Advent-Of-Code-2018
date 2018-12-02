# Reads data
file = open("02 input.txt")
ids = (file.readlines())
for x in range(0, len(ids)):
    ids[x] = ids[x].replace("\n", "")

# Part 1
counts = []
twos = 0
threes = 0
for box_id in ids:
    letters = list(box_id)
    # Count occurences of each letter
    found = {"": 0}
    for letter in letters:
        if letter in found:
            found[letter] += 1
        else:
            found[letter] = 1
    count = [0, 0]
    for letter in found:
        if found[letter] == 2:
            twos += 1
            break
    for letter in found:
        if found[letter] == 3:
            threes += 1
            break
print("Checksum is: " + str(twos * threes))

# Part 2
# Loop through ids
for box_id in ids:
    for check in ids:
        if box_id == check:
            continue
        life = False
        pos = 0
        found = True
        # Loop through each letter in id and check if same
        for x in range(0, len(box_id)):
            if box_id[x] != check[x]:
                if life:
                    found = False
                    continue
                else:
                    life = True
                    pos = x
        if found:
            print("Match found")
            word = ""
            # Rebuild id
            for x in range(0, len(check)):
                if x == pos:
                    continue
                word += check[x]
            print(word)
            exit()
