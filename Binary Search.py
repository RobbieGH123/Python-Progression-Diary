# Binary Search for future reference:

def binary_search(arr, target): # 2 Parameters, one for array and one for the target
    left = 0                    # Left Counter
    right = len(arr) - 1        # Right Counter

    while left <= right:        # While the left counter is smaller than or equal to the right counter
        mid = (left + right) // 2 # The midpoint can be found in betweent them
        
        if arr[mid] == target:   # If at the midpoindth index of the array is the target
            return mid  # Found it!
        elif arr[mid] < target:  # Else, if the midpointh index is too small, we know that
            left = mid + 1  # Target is in the right half
        else:               # If not, then we definitelty know that
            right = mid - 1  # Target is in the left half

    return -1  # Not found

# Example usage
numbers = [1, 3, 5, 7, 9, 11]
target = 7

index = binary_search(numbers, target)
print(f"Target {target} found at index {index}")
