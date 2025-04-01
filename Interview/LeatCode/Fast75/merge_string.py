'''Algorithm
1️⃣ Initialize an empty result list.
2️⃣ Use a for loop to pick characters alternately.
3️⃣ Append any remaining characters if one string is longer.
4️⃣ Convert the list to a string and return.'''

def merge_alternately(word1, word2):
    result = []
    length = max(len(word1), len(word2))  # Get the max length

    for i in range(length):
        if i < len(word1):  
            result.append(word1[i])  # Add from word1
        if i < len(word2):  
            result.append(word2[i])  # Add from word2
    
    return "".join(result)  # Convert list to string

# Example usage
print(merge_alternately("abc", "pqr"))     # Output: "apbqcr"
print(merge_alternately("ab", "pqrs"))     # Output: "apbqrs"
print(merge_alternately("abcd", "pq"))     # Output: "apbqcd"

'''Time Complexity: O(n) (Processes each character once)
Space Complexity: O(n) (Stores merged string in a list)'''
