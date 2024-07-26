f = [[i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if target - nums[i] == nums[j]]
return (f[0])
