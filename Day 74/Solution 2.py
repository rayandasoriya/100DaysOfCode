from collections import Counter

class Solution:
    def combinationSum2(self, candidates, target):
        """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
        def rec(combi, target_rem, i_cand):
            if target_rem == 0:
                all_combis.append(list(combi))
                return
            if target_rem < 0:
                return
            if i_cand == len(cands_counts):
                return
            rec(combi, target_rem, i_cand+1)  # we don't take the current number
            cand, count = cands_counts[i_cand]
            for n in range(1,count+1):  # we take the current number n times
                combi.append(cand)
                target_rem -= cand
                rec(combi, target_rem, i_cand+1)
            for n in range(1,count+1):
                combi.pop()
        
        all_combis = []
        cands_counts = list(Counter(candidates).items())
        rec([], target, 0)
    return all_combis
