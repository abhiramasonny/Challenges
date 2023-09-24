def fixedlargestSubArray(arr,k):
    
    curr_subarray = sum(arr[:k])
    res = [curr_subarray]
    
    for i in range(1,len(arr)-k+1):
        curr_subarray = curr_subarray - arr[i-1]
        curr_subarray = curr_subarray + arr[i+k-1]
        
        res.append(curr_subarray)
    return res
print(fixedlargestSubArray([2,-8,3,10,10],4))
