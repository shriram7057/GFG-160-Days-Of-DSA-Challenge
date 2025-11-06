class Solution:
    def closest3Sum(self, arr, target):
        arr.sort()
        n = len(arr)
        closest = float('inf')

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]

                # Update closest if this sum is nearer to target
                if abs(target - curr_sum) < abs(target - closest):
                    closest = curr_sum

                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return target  # Exact match

        return closest
