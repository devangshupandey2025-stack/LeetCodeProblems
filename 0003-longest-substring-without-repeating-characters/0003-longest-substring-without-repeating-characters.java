class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        int maxLength = 0;
        boolean[] charSet = new boolean[256];
        int left = 0;

        for (int right = 0; right < n; right++) {
            if (!charSet[s.charAt(right)]) {
                charSet[s.charAt(right)] = true;
                maxLength = Math.max(maxLength, right - left + 1);
            } else {
                while (charSet[s.charAt(right)]) {
                    charSet[s.charAt(left)] = false;
                    left++;
                }
                charSet[s.charAt(right)] = true;
            }
        }

        return maxLength;
    }
}