#User function Template for python3

class Solution:    
    #Complete this function
    def printNos(self,n):
        #Your code here
        if n<1:
            return
        self.printNos(n-1)
        print(n, end=' ')


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        ob = Solution()

        ob.printNos(N)
        print()
        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends