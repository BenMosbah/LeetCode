class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            l = len(s)
            j = 0
            mapping = {}
            mapped = set()
            for i in range(l):
                ant = s[i]
                if mapping.get(ant,'Nope') == 'Nope':
                    # we found a letter that is not mapped to anything
                    while j < l and t[j] in mapped  :
                        # target is already reached and application need to be
                        # injective
                        j += 1
                    if j == l:
                        # no more elements in the image set
                        break
                    else:
                        # map the ith of s  letter to the jth letter of t
                        mapping[ant] = t[j]
                        mapped.add(t[j])
                        j += 1
            return ''.join([mapping.get(s_c,'') for s_c in s]) == t
