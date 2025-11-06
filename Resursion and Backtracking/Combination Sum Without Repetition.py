class Solution:
    def uniqueCombinations(self, arr, target):
        result = []
        arr.sort()

        def backtrack(start, path, total):
            if total == target:
                result.append(list(path))
                return
            if total > target:
                return

            for i in range(start, len(arr)):
                # Skip duplicates
                if i > start and arr[i] == arr[i - 1]:
                    continue
                path.append(arr[i])
                backtrack(i + 1, path, total + arr[i])  # move to next index
                path.pop()

        backtrack(0, [], 0)
        return result
