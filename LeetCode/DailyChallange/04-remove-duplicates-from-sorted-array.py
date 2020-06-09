nums = [1,1,3]  #[0,0,1,1,1,2,2,3,3,4]
def removeDuplicates(nums):
    # list1 = []
    # if len(nums) == 0 or len(nums) == 1:
    #     return 0
    # for i in range(len(nums)):
    #     if nums[i] not in list1:
    #         list1.append(nums[i])
    # return len(list1)
    def removeDuplicates(self, nums):
        len_ = 1
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[len_] = nums[i]
                len_ +=1
        return len_

print(removeDuplicates(nums))

