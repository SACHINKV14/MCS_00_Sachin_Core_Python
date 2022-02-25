def miniMaxSum(arr):
    a=sum(arr)
    print(a-arr[0]," ",a-arr[-1])
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
