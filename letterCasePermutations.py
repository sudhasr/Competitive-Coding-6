# Accepted on leetcode
# Time complexity - O(2^N) since we take decision of lower or upper at every letter
# Space complexity - O(N) if we consider recursive stack, even otherwise O(N) since we create two new lists

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        list_S = []
        list_S.extend(S)#Convert string to array of characters
        #Edge Case
        if len(S) == 0 or S == None:
            return []
        self.backtrack(res, list_S, 0)
        return res
    
    def backtrack(self, res, list_S, index):
        #Base case
        if index == len(list_S):
            s = ''.join(list_S)
            res.append(s)
            return
        if list_S[index].isalpha():
            #Lower case
            list_S[index] = list_S[index].lower()
            self.backtrack(res, list_S, index+1)
            #Upper case
            list_S[index] = list_S[index].upper()
            self.backtrack(res, list_S, index+1)
        else:
			#Check if it is a number
            self.backtrack(res, list_S, index+1)