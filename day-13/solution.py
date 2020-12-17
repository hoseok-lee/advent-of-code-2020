from functools import reduce



'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("bus-times.txt", "r")
raw_file = f.read().split("\n")

# Split text into time and bus schedule
current_time = int(raw_file[0])
true_bus_times = [
    int(x)  \

    for x in (raw_file[1].replace("x", "0")).split(",") \
]

# Remove all "x" bus times
# Only necessary for part 1
stripped_bus_times = [ \
    bus_time \
    
    for bus_time in true_bus_times \
    if bus_time != 0 \
]



'''
    PART 1: DETERMINE CLOSEST MULTIPLE

    Complexity: O(n)

    This is a brute force algorithm that calculates the lowest multiple of 
    every bus's schedule time greater than the current time, and chooses the
    closest bus. 
'''
'''
# Calculate the fastest bus
fastest_bus = min([[bus_time - (current_time % bus_time), bus_time] \
                    for bus_time in stripped_bus_times])

print(fastest_bus[0] * fastest_bus[1])
'''


'''
    PART 2: DETERMINE EARLIEST INCLUSIVE MULTIPLE

    Complexity: O(n)

    The problem can be broken down into the Chinese remainder theorem by
    observing that the indices of the bus represent the remainders, and the bus
    numbers represent the modulus. By setting up a system of equations such that

        x = b_0 mod n_0,
        x = b_1 mod n_1,
        ...
        x = b_k mod n_k

    the number x that satisfies all of these equations will represent the first
    time slot with all of the buses spaced exactly by their indices.
'''

# Co-prime product
co_prime_product = reduce(lambda x, y: x * y, stripped_bus_times)

# Bus times with their proposed remainders
remainder_bus_times = [ \
    [(bus_time - bus_index), bus_time] \

    for bus_index, bus_time in enumerate(true_bus_times) if bus_time != 0 \
]

# Calculate using Chinese remainder theorem
print(sum([ \
    remainder * int(co_prime_product / modulus) * \
        pow(int(co_prime_product / modulus), -1, modulus)

    for remainder, modulus in remainder_bus_times \
]) % co_prime_product)