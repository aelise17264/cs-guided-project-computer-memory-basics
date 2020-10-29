"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    valid = True
    for char in string:
        if char not in alpha + upper:
            valid = False
    if valid:
        result = ""
        for char in string:
            if char in alpha:
                result += char
            else:
                for i in range(len(upper)):
                    if char == upper[i]:
                        result += alpha[i]
    return result

    # encoded_chars = []
    # for char in string:
    #     encoded_chars.append(ord(char))

    # for i in range(len(encoded_chars)):
    #     if encoded_chars[i] > 64 and encoded_chars[i] < 91:
    #         encoded_chars[i] += 32

    # decoded_chars = []
    # for n in encoded_chars:
    #     decoded_chars.append(chr(n))

    # return "".join(decoded_chars)

print(to_lower_case("LambdaSchool"))
print(to_lower_case("LLAMA"))