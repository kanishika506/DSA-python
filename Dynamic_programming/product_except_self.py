nums=[]  #given
left=[]
right=[]
back=1
current=1
result=[]
for i range(0,len(nums)):
		left.append(current)
		current*=nums[i]
for i range(len(nums)-1,-1,-1):
		right.append(back)
		back*=nums[j]
right.reverse()
result=left*right
return result

#this is  0(n) space three times over
# we need it to be o(1) space solution

nums=[]  #given
result=[]
current , back = 1 , 1
for i range (0,len(nums)):
		result,append(current)
		current*=nums[i]
for j in range(len(nums)-1  ,-1 , -1):
		result[j]*=back
		back*=nums[j]
return result

# we went from  three arrays to one array 
