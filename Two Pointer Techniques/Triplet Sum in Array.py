class Solution:
    def hasTripletSum(self, arr, target):
        arr.sort()
        n = len(arr)

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                if curr_sum == target:
                    return True
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

        return False
