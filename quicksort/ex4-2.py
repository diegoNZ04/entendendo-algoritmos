def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])
    
nArr = [4, 7, 8]

print(count(nArr))