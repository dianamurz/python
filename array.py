def array_plus_array(arr1, arr2):
    #return sum(arr1+arr2)
    res = 0
    for i in arr1 + arr2:
        res += i
    return res

res = array_plus_array([1,2,3], [4,5,6])
print(res)
