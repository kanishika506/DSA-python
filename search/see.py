#search in rotated sorted array and if not in array return -1
nums=[]  #given
target=0 #given
left=0
right=len(nums)-1
while left <=right:
	mid=left+(right-left)//2
	if nums[mid]==target:
		return mid
	elif nums[mid]>nums[right] and nums[left]<=target<nums[mid]:
		right=mid-1
	elif nums[mid]>nums[right] and not(nums[left]<=target<nums[mid]):
		left=mid+1
	elif nums[mid]<nums[right] and nums[mid]<target<=nums[right]:
		left=mid+1
	elif nums[mid]<nums[right] and not(nums[mid]<target<=nums[right]):
		right=mid
	else:
		right-=1
return -1
