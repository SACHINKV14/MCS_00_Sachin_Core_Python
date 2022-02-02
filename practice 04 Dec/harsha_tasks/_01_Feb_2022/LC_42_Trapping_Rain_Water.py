"""42. Trapping Rain Water

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
"""

# Python3 implementation of the approach

# Function to return the maximum
# water that can be stored
def maxWater(arr, n):

    # To store the maximum water
    # that can be stored
    res = 0

    # For every element of the array
    for i in range(1, n - 1):

        # Find the maximum element on its left
        left = arr[i]
        for j in range(i):
            left = max(left, arr[j])

        # Find the maximum element on its right
        right = arr[i]

        for j in range(i + 1, n):
            right = max(right, arr[j])

        # Update the maximum water
        res = res + (min(left, right) - arr[i])

    return res

# Driver code
if __name__ == "__main__":
    # arr = [4,2,0,3,2,5]
    arr=[0,1,0,2,1,0,1,3,2,1,2,1]
    n = len(arr)

    print(maxWater(arr, n))

