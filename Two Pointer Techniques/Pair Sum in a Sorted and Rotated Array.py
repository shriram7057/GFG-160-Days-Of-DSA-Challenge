class Solution:
    def pairInSortedRotated(self, arr, target):
        n = len(arr)

        # Step 1: Find the pivot (index of largest element)
        for i in range(n):
            if arr[i] > arr[(i + 1) % n]:
                break
        pivot = i

        # Step 2: Set left and right pointers
        left = (pivot + 1) % n  # smallest element
        right = pivot           # largest element

        # Step 3: Search for the pair
        while left != right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                return True
            elif curr_sum < target:
                left = (left + 1) % n
            else:
                right = (n + right - 1) % n

        return False
