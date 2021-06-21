#easy implementation by tailwind

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    nflag, lflag,uflag,sflag = 0,0,0,0
    for i in password:
        if i in numbers:
            nflag=1
        if i in lower_case:
            lflag=1
        if i in upper_case:
            uflag=1
        if i in special_characters:
            sflag=1
    ansL = [nflag, lflag, uflag, sflag]
    
    ans = ansL.count(0) 
    
    if (n+ans)<6:
        return 6-n
    else:
        return ans
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
