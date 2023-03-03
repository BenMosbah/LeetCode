class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        num_letters = len(beginWord)
        wordList = [w for w in wordList if len(w) == num_letters]

        # doesn't deal with the case where words are identical
        # but this should not be an issue
        def dist_is_one(word1, word2):
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                    if diff >= 2:
                        return False
            return True

        def dfs(beginWord, endWord, wordList, sequence, sequences_found):
            if endWord not in wordList:
                return
            else:
                if dist_is_one(beginWord, endWord):
                    sequences_found.append([endWord] + sequence)
                else:
                    candidate_endWords = [w for w in wordList if dist_is_one(w, endWord)]
                    if len(candidate_endWords) == 0:
                        return
                    else:
                        for new_endWord in candidate_endWords:
                            dfs(beginWord, new_endWord, [w for w in wordList if w != endWord], [endWord] + sequence,
                                sequences_found)

        sequences_found = []
        dfs(beginWord, endWord, wordList, [], sequences_found)
        shortest = 0
        if len(sequences_found) > 0:
            shortest = min([len(s) for s in sequences_found])
        shortest_sequences = [s for s in sequences_found if len(s) == shortest]
        return [[beginWord] + s for s in shortest_sequences]