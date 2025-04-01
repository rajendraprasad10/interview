'''Approach: Using GCD Function
Algorithm
1️⃣ Check if str1 + str2 == str2 + str1 → If not, return "" (No common prefix).
2️⃣ Find the greatest common divisor (GCD) of the lengths of str1 and str2.
3️⃣ Return the substring of str1 from 0 to GCD length.'''


from math import gcd

def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:  
        return ""  # No common divisor
    
    gcd_length = gcd(len(str1), len(str2))  # Get GCD of lengths
    return str1[:gcd_length]  # Return substring of that length

# Example usage
print(gcd_of_strings("ABCABC", "ABC"))     # Output: "ABC"
print(gcd_of_strings("ABABAB", "ABAB"))    # Output: "AB"
print(gcd_of_strings("LEET", "CODE"))      # Output: ""


'''Time Complexity: O(N)
Space Complexity: O(1)'''


def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:  
        return ""  # No common divisor exists
    
    # Start with the shorter string as the largest possible divisor
    min_length = min(len(str1), len(str2))
    
    # Check decreasing lengths until a valid divisor is found
    for i in range(min_length, 0, -1):  
        if len(str1) % i == 0 and len(str2) % i == 0:  # Check divisibility
            candidate = str1[:i]  # Possible common substring
            if str1 == candidate * (len(str1) // i) and str2 == candidate * (len(str2) // i):
                return candidate  # Return the largest valid divisor
    
    return ""  # No valid divisor found

# Example usage
print(gcd_of_strings("ABCABC", "ABC"))     # Output: "ABC"
print(gcd_of_strings("ABABAB", "ABAB"))    # Output: "AB"
print(gcd_of_strings("LEET", "CODE"))      # Output: ""

'''
Example 1:
str1 = "ABCABC", str2 = "ABC"
✅ "ABCABC" + "ABC" == "ABC" + "ABCABC"
✅ "ABC" is a valid divisor because:

"ABCABC" = "ABC" × 2

"ABC" = "ABC" × 1

✅ Answer: "ABC"

'''

'''Time Complexity: O(N)
Space Complexity: O(1)'''