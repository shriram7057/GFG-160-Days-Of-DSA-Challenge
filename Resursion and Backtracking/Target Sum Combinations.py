class Solution:
    def targetSumComb(self, arr, target):
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(arr)):
                path.append(arr[i])
                backtrack(i, path, total + arr[i])  # allow reuse of same element
                path.pop()

        backtrack(0, [], 0)
        return result
