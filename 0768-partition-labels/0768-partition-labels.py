class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        #build a hashmap to store the end index of the each characters
        #iterate throught each characters and update the end index, if the end index similar to the current one add the size to the final result
        last_idx = {}
        for i, c in enumerate(s):
            last_idx[c] = i
        
        result = []
        size = 0
        end = 0

        for i, c in enumerate(s):
            end = max(end, last_idx[c])
            size += 1

            if i == end:
                result.append(size)
                size = 0
        return result


        # hash_map = {}
        # end_idx = 0
        # size = 0
        # result = []
    
        # for i in range(len(s)):
        #     hash_map[s[i]] = i

        # for i in range(len(s)):
        #     end_idx = max(end_idx, hash_map[s[i]])
        #     size += 1
        #     if i == end_idx:
        #         result.append(size)
        #         size = 0
        # return result


        