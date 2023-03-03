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

        #return [[beginWord] + s for s in shortest_sequences]

        ##### DFS solution
        if endWord not in wordList :
            return []
        else:
            found = False
            chain_candidates = [[endWord]]
            depth = 1
            final_chains = []
            while not found and depth < len(wordList):
                to_build_new_chain_candidates = []
                for chain in chain_candidates:
                    available_words = wordSet-set(chain)
                    new_endword = chain[0]
                    new_chains = []
                    if dist_is_one(beginWord,new_endword):
                        final_chains.append([beginWord]+chain)
                        found = True
                    else:
                        neighbors = [w for w in available_words if dist_is_one(w,new_endword)]
                        if len(neighbors) == 0 :
                            pass
                        else:
                            new_chains = [[neighbor]+chain for neighbor in neighbors]
                    to_build_new_chain_candidates += new_chains
                depth += 1
                chain_candidates = to_build_new_chain_candidates
            return final_chains