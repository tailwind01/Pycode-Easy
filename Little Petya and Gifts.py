    numFriends = int(input())
    giftsOut = list(map(int,input().rstrip().split()))
     
    rcpt = []
     
    for i in range(numFriends):
        rcpt+=[str(giftsOut.index(i+1)+1)]
     
    print(" ".join(rcpt))

one testcase:
78

17 50 30 48 33 12 42 4 18 53 76 67 38 3 20 72 51 55 60 63 46 10 57 45 54 32 24 62 8 11 35 44 65 74 58 28 2 6 56 52 39 23 47 49 61 1 66 41 15 77 7 27 78 13 14 34 5 31 37 21 40 16 29 69 59 43 64 36 70 19 25 73 71 75 9 68 26 22