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

