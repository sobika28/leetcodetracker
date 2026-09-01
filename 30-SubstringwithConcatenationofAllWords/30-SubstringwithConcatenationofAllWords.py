# Last updated: 9/1/2026, 9:12:54 PM
1class Solution:
2    def findSubstring(self, s, words):
3        if not s or not words:
4            return []
5        word_len = len(words[0])
6        word_count = len(words)
7        total_len = word_len * word_count
8        if total_len > len(s):
9            return []
10        freq = {}
11        for word in words:
12            freq[word] = freq.get(word, 0) + 1
13        ans = []
14        for i in range(word_len):
15            left = i
16            count = 0
17            current = {}
18
19            for right in range(i, len(s) - word_len + 1, word_len):
20                word = s[right:right + word_len]
21
22                if word in freq:
23                    current[word] = current.get(word, 0) + 1
24                    count += 1
25
26                    while current[word] > freq[word]:
27                        left_word = s[left:left + word_len]
28                        current[left_word] -= 1
29                        left += word_len
30                        count -= 1
31
32                    if count == word_count:
33                        ans.append(left)
34
35                        left_word = s[left:left + word_len]
36                        current[left_word] -= 1
37                        left += word_len
38                        count -= 1
39
40                else:
41                    current = {}
42                    count = 0
43                    left = right + word_len
44
45        return ans