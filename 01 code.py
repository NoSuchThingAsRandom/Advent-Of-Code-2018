import time

start = time.time()
file = open("01 input.txt")
nums = (file.readlines())
frequency = 0
reached = {0}  # Uses a set because it is way faster than a list


# (2500 times faster)

def frequency_pass(freq, done):
    for value in nums:
        freq += int(value)

        if freq in done:
            print("This is the first frequency: " + str(freq))
            return ""
        else:
            done.add(freq)
    return [freq, done]


# Calculates the first sum
result = frequency_pass(frequency, reached)
print("Sum is: " + str(result[0]))
# Loops until it finds the change
while result != "":
    result = frequency_pass(result[0], result[1])
print("Time taken was: " + str(time.time() - start))
