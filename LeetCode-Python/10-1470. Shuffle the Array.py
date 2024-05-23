class Solution(object):
  def shuffle(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: None
    """
    l, r = 0, n
    myArray = []
    
    for _ in range(n):
        myArray.append(nums[l])
        myArray.append(nums[r])
        l += 1
        r += 1
    return myArray