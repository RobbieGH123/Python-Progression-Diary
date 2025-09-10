def remove_duplicates(nums):
 k = 1
 if not nums:
    return(0)
 else: 
  for i in range(1, len(nums)):
   if nums[i] != nums[i-1]:
     nums[k] = nums[i]
     k += 1 
 return k 
nums = [1,1,2]
result = remove_duplicates(nums)
print(f" {result}: {nums[:result]}")

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    
    sorted_s = sorted(s)
    sorted_t = sorted(t)  
    
    if sorted_s == sorted_t:
        return True 
    else:
        return False

       
 
             
    



     

