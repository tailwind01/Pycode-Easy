arr = list(map(int, input().rstrip().split()))
arr.sort()
bigg = max(arr)
ansAr = []

for i in arr[:-1]:
    ansAr+=[str(bigg-i)]

print(" ".join(ansAr))
