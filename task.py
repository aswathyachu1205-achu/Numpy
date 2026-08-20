import numpy as np

arr = np.array([
    [10,25,30,45],
    [15,20,35,40],
    [50,60,55,70],
    [80,75,90,65]
])

print(arr)

print(arr.ndim)

print(arr.shape)

print(arr.size)

print(arr.dtype)

print(arr[1,2])

print(arr[0,:])

print(arr[3,:])

print(arr[:,0])

print(arr[:2,1:3])

print(np.sum(arr))

print(np.max(arr))

print(np.min(arr))

print(np.mean(arr))

print(np.sum(arr,axis = 1))

print(np.sum(arr,axis = 0))

print(np.argmax(arr))

print(np.argmin(arr))

print(np.sort(arr,axis = 1))

print(np.argsort(arr,axis = 1))

print(np.square(arr))

print(np.sqrt(arr))

print(arr.reshape(2,8))

