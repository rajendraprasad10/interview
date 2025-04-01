# First Reverse
# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH.
# Examples
# Input: "coderbyte"
# Output: etybredoc


'''
Read the input string 
reserve the each word in a string
split the string into list of words
join the all the words to string 
'''


def FirstReverse(strParam):

    # strParam = strParam[::-1]
    # print(strParam)
  
    strParam = [word[::-1] for word in strParam.split()]
    print(strParam)

    reversed_string = ' '.join(strParam) 
    return reversed_string

# keep this function call here 
print(FirstReverse(input()))