class Solution:
    def generateIp(self, s):
        def isValid(segment):
            # Segment must be between 0 and 255, no leading zeros unless it's '0'
            return len(segment) > 0 and int(segment) <= 255 and (segment == "0" or not segment.startswith("0"))

        n = len(s)
        result = []

        for i in range(1, min(4, n - 2)):
            for j in range(i + 1, min(i + 4, n - 1)):
                for k in range(j + 1, min(j + 4, n)):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if all(map(isValid, [a, b, c, d])):
                        result.append(f"{a}.{b}.{c}.{d}")

        return result
