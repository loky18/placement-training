    def bubbleSort(arr):
        n=len(arr)
        for i in range(n):
            for j in range(0,n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]

    arr=[7,2,8,1,5]
    bubbleSort(arr)
    print("Sorted array:",arr)
