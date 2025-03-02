#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List
import math


# } Driver Code Ends


#User function Template for python3

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        oa,ob=a,b
        hcf=0
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
                
        if a == 0:
            hcf=b
        else:
            hcf=a
            
        lcm=(oa*ob)//hcf
        return [lcm, hcf]
    
                                
                            


#{ 
 # Driver Code Starts.


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        obj = Solution()
        res = obj.lcmAndGcd(a, b)
        print(f"{res[0]} {res[1]}")
        print("~")

# } Driver Code Ends