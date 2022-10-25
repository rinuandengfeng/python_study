import copy

#copy模块里面有copy和deepcopy两个函数，分别用来对数据惊醒深复制和浅复制


nums = [1,5,3,8,[100,200,300,400],6,7]

nums1 = copy.copy(nums)      #对nums列表进行浅复制

nums2 = copy.deepcopy(nums)     #对nums列表进行深复制


print(nums1)

print(nums2)
