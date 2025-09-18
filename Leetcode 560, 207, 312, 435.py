# Leetcode: 560, 207, 312, 435

# Leetcode 560: Subarray Sum Equals K
# Given an array & an integer (K) return the total number of subarrays which have a sum of K

def subarray_k(lst, k):
    
    counter = 0

    for start in range(len(lst)):
        for end in range(start, len(lst)):

            if sum(lst[start:end+1]) == k:
                counter += 1
    return counter

print(f"The number of subarrays whose sums are equal to K is: {subarray_k([0, 1, 2, 3, 4, 5], 5)}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        
# Leetcode 207: Course Schedule:

def canfinish(numcourses, prerequisites):    # Creates a Function that prepares to take the number of courses, and the prerequisite for those courses as parameters.
    
    # Within the variable, called 'graph'
    graph = [[] for _ in range(numcourses)]  # Create an empty list '[]' for every number in range(numofcourses) e.g. numofcourses = 3 -> 0, 1, 2 -> [][][]

    for course, prereq in prerequisites:       # For each course & prequisite in 'prerequisites' 
                                               # 'course' and 'prereq' are both arbitrary here - Course reads the 1st value of each prerequisite, prereq reads the 2nd.
    
     graph[course].append(prereq)              # Goes to the list at position course and adds prereq to it. [1,0] -> graph[1].append[0] -> [][0][]

    states = [0 for _ in range(numcourses)]    # Create a list of 0s for tracking course exploration states: 0=unvisited, 1=currently exploring, 2=fully explored

    for course in range (numcourses):          # Loop through each course number from 0 to numcourses-1
        if hasCycle(course, graph, states):    # If hasCycle function returns True (cycle found)
            return False                       # Then return False from the canfinish function (impossible schedule)
    return True                                # If NO courses have cycles, return True from the canfinish function (possible schedule)

def hasCycle(course, graph, states):           # Creates a helper function that checks if a specific course leads to a cycle by following its prerequisites.
    if states[course] == 2:                    # If course is already fully explored (state 2), no cycle here
        return False                           # Safe to return False - we've checked this path before
    if states[course] == 1:                    # If course is currently being explored (state 1), we found it again = CYCLE!
        return True                            # Return True because we're stuck in a loop
    states[course] = 1                         # Mark current course as "currently exploring" to detect if we come back to it

    for prereq in graph[course]:               # Loop through all prerequisites that this course depends on
        if hasCycle(prereq, graph, states):    # Recursively checks each prerequisite for cycles. This is where the function calls itself to follow the dependency chain.
            return True                        # If ANY prerequisite has a cycle, this course does too
        
    states[course] = 2                         # Mark course as fully explored - all its paths are cycle-free
    return False                               # No cycles found in this course's dependency chain
print(f"{canfinish(5, [[0,1], [2,0]])}")
        

"""
- states[2] == 0, so continue
- states[2] = 1 (mark as exploring)
- graph[2] = [1], so check prereq 1  
  - hasCycle(1, graph, states):
    - states[1] == 2 (already done), return False
- states[2] = 2 (mark as done)
- return False
states now: [2, 2, 2, 0]
"""