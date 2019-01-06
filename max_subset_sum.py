def maxSubsetSum(arr):
    include = 0
    exclude = 0
    for i in arr: 
        new_exclude = exclude if exclude>include else include 
        include = exclude + i 
        exclude = new_exclude 
      
    return (exclude if exclude>include else include) 

arr = [-2, 1, 3, -4, 5]
maxSubsetSum(arr)