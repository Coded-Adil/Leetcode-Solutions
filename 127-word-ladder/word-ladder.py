from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()

            for i in range(len(word)):
                original_char = word[i]

                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if letter == original_char:
                        continue

                    new_word = word[:i] + letter + word[i + 1:]

                    if (
                        new_word in word_set
                        and new_word not in visited
                    ):
                        if new_word == endWord:
                            return level + 1

                        queue.append((new_word, level+1))
                        visited.add(new_word)

        return 0
