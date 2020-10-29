"""
Given an unsigned integer, write a function that returns the number of '1' bits
that the integer contains (the
[Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight))

Examples:

- `hamming_weight(n = 00000000000000000000001000000011) -> 3`
- `hamming_weight(n = 00000000000000000000000000001000) -> 1`
- `hamming_weight(n = 11111111111111111111111111111011) -> 31`

Notes:

- "Unsigned Integers (often called "uints") are just like integers (whole
numbers) but have the property that they don't have a + or - sign associated
with them. Thus they are always non-negative (zero or positive). We use uint's
when we know the value we are counting will always be non-negative."
"""

#n is going to be a normal intiger & we are going to return an intiger
def hamming_weight(n):
    # Your code here
    #if we're given a "normal" unsigned intiger, how do we convert it to a bitwise representation?
    #bitwise logical operators `&&`, `||` in js
    #bitwise logical operators: `&`, `|`

    #using & we have a way to check the rightmost bit of n to see if it equals 1
    #the left & right shift operations
    #<< or >>
    #if & on the rightmost digit returns a 1, increment a counter
    # >> by 1 bitwise digit
    counter = 0
    #when do we stop right shifting?
    #we can stop right shifting when n ==0

    #way 1
    # while n != 0:
    #     if n & 1 == 1:
    #         counter += 1
    #     #do the right shift
    #     n = n>>1

    #return the number of 1s in the bitwise representation of the number

    #way 2
    # bin_representation = bin(n)

    # for i in range(len(bin_representation)):
    #     if bin_representation[i] == '1':
    #         counter += 1

    # return counter

    #way 3
    return bin(n).count("1")
print(hamming_weight(20))