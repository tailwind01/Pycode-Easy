#/ tailwind: code to find sum of 'curious' numbers as per the problem statement for problem 34 of Project Euler
factlist = [1,1] #factorial list initiated
for i in range(2,10): #factorial list derived for each digit of any number
    factlist.append(factlist[-1]*i)
maxnum = factlist[-1]             #by hypothesis, any number greater than 9! cannot possibly have a sum of digit factorials equaling number since number of 0's will increase quite a lot and 0! is 1, which is an abysmal addition

ansnums = []
for j in range(3,maxnum):
    jstr = str(j)
    tmsum = 0
    for d in jstr:
        relind = int(d)
        tmsum+=factlist[relind]
    if tmsum==j:
        ansnums+=[j]

print(sum(ansnums))
