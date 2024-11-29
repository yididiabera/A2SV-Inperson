class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        #sort the people to easily find the lightest and the heaviest person
        #use two ptrs and pair the lightest and the heaviest person, if it exceeds the limit, use the boat for only the heaviest person

        people.sort()
        l, r = 0, len(people) - 1
        boat = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boat += 1
        return boat