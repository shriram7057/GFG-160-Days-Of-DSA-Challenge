class Solution:
    def possibleWords(self, arr):
        # Keypad mapping
        keypad = {
            2: "abc", 3: "def", 4: "ghi", 5: "jkl",
            6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"
        }

        result = []

        def backtrack(index, path):
            if index == len(arr):
                result.append(path)
                return
            for char in keypad[arr[index]]:
                backtrack(index + 1, path + char)

        if arr:
            backtrack(0, "")
        return result
