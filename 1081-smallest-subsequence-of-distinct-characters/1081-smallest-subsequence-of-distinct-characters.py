class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        k = []
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                continue

            while len(k) > 0 and k[-1] > s[i] and last[k[-1]] > i:
                seen.pop(k.pop())

            k.append(s[i])
            seen[s[i]] = True

        return "".join(k)