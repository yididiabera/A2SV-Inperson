class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        #INSERTION SORT
        length = len(heights)

        for i in range(1, length):
            h_key = heights[i]
            n_key = names[i]
            j = i - 1

            while(j >= 0 and heights[j] < h_key):
                heights[j + 1] = heights[j]
                names[j + 1] = names[j]
                j = j - 1
            heights[j + 1] = h_key
            names[j + 1] = n_key

        return names
        
        #SELECTION SORT
        # length = len(heights)
        # for i in range(0, length - 1):
        #     cur_idx = i
        #     for j in range(i + 1, length):
        #         if heights[j] > heights[cur_idx]:
        #             cur_idx = j
        #     if i != cur_idx:
        #         heights[i], heights[cur_idx] = heights[cur_idx],heights[i]
        #         names[i], names[cur_idx] = names[cur_idx], names[i]
        # return names
        
        
        #BUBBLE SORT
        # length = len(heights)
        # for i in range(0, length - 1):
        #     swapped = False
        #     for j in range(0, length - i - 1):
        #         if heights[j] < heights[j + 1]:i
        #             heights[j + 1], heights[j] = heights[j], heights[j + 1]
        #             names[j + 1], names[j] = names[j], names[j + 1]
        #             swapped = True
        #     if not swapped:
        #         break
        # return names


        # people = list(zip(heights, names))
        # sorted_people = sorted(people, reverse=True)
        # sorted_names = [person[1] for person in sorted_people]
        # return sorted_names