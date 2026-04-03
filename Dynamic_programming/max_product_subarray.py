#return subarray with largest product
nums=[]			#given
maxi, mini,result=nums[0],nums[0], nums[0]
for i in range(1,len(nums)):
	temp=maxi
	temp2=mini
	maxi=max(nums[i],temp*nums[i],temp2*nums[i])
	mini=min(nums[i],temp*nums[i], temp2*nums[i])
	result=max(mini,maxi,result)
return result
