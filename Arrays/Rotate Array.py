#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        n = len (arr)
        d = d % n 
        arr[:] = arr[d:] + arr[:d]