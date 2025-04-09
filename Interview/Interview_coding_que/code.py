# find the second larget element 
'''Explanation:
Initialization:

Variables largest and second_largest are initialized to negative infinity.

The loop index i starts from 0.

Loop:
The while loop iterates through all elements of lst, performing constant-time operations for each element:

Checking if the current element is greater than largest.

Updating largest and second_largest if necessary.

Incrementing i.

Iteration Count:

The loop runs exactly once for each element in the list, i.e., 𝑛 n iterations.

Per-Iteration Operations:

Inside the loop, there are only comparisons and assignments, which are 𝑂(1) O(1) operations.
Total Time Complexity:
Since the loop executes 
𝑛 n iterations and each iteration involves 𝑂(1)
O(1) operations, the overall time complexity is: 𝑂(𝑛) O(n)
'''
lst = [10,20,30,40,50]

largest = second_largest = float('-inf')

i = 0 

while i < len(lst):
    if lst[i] > largest:
        
        second_largest = largest 
        largest = lst[i]
        
    elif lst[i] > second_largest and lst[i] != largest:
        second_largest = lst[i]
        
    i+=1

print("second largest", second_largest)

######   Brute Force Approach (O(n²)) #####

'''Algorithm
Iterate through each element (i) in the list.

For each element (i), iterate through all the next elements (j).

If nums[i] + nums[j] == target, return [i, j].

If no pair is found, return an empty list.'''

def two_sum(nums, target):
    n = len(nums)
    for i in range(n):  # First loop
        for j in range(i + 1, n):  # Second loop (avoid duplicate pairs)
            if nums[i] + nums[j] == target:  # Check if sum matches target
                return [i, j]  # Return the indices

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]

'''Time & Space Complexity
Time Complexity: O(n²) (Two nested loops)

Space Complexity: O(1) (No extra space used)'''

'''Hash Map (O(n)) → Best Approach
We use a dictionary (hash map) to store numbers we have seen so far along with their indices.
This allows us to check for the complement (target - num) in O(1) time.'''

def two_sum(nums, target):
    num_map = {}  # Dictionary to store value:index pairs

    for i, num in enumerate(nums):
        complement = target - num  # Find the needed number
        if complement in num_map:
            return [num_map[complement], i]  # Return indices
        num_map[num] = i  # Store the current number in the dictionary

'''Time Complexity: O(n) (Best solution )
Space Complexity: O(n) (Extra space for dictionary)'''

# Example usage
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]

'''Summary
Approach	Time Complexity	Space Complexity	Best For
Brute Force	O(n²)	O(1)	Small inputs
Hash Map	O(n)	O(n)	Large inputs (Best solution)'''

'''
Code Functionality:
Input Dictionaries:

d1 = {'a': 10, 'b': 20}

d2 = {'b': 20, 'c': 40}

Objective:

Add the values of keys that exist in both dictionaries.

Include keys that are unique to one dictionary with their original values.

Approach:

Use a while loop to iterate through all unique keys obtained by the union of d1 and d2 keys.

Use the dict.get(key, default) method to handle cases where a key is missing from one dictionary (defaulting to 0).

'''


d1 = {'a' : 10, 'b' : 20}
d2 = {'b' : 20, 'c': 40}
# Add two dictionaries
# while loop 

#Initiate the dict1
result = {}

# get all the unique for both dicts
keys = list(set(d1.keys()).union(d2.keys()))

i = 0 
while i < len(keys):
    key = keys[i]
    result[key] = d1.get(key,0) + d2.get(key,0)
    i+=1
print("added dict",result)


# print the flat list from nested list
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

flat_list = flatten_list([[1,2],[3,4]])
print("====flatlist", flat_list)

'''
how you can create two decorators to modify the behavior of a sum function as described:

A decorator that subtracts 1 from the result.

A decorator that multiplies the result by 2.
'''

def subtract_one(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result - 1
    return wrapper

def multiply_by_two(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@multiply_by_two
@subtract_one
def sum(a, b):
    return a + b

# Testing
print(sum(3, 4))  # ((3 + 4) - 1) * 2 = 12
