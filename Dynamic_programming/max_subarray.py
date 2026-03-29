num=[]
total_sum=float('-inf')
for i in range(0,len(num)):
		for j in range(i+1,len(num)+1):
				sub=num[i:j]
				if sum(sub)>total_sum:
						total_sum=sum(sub)
return total_sum

#this is O(n²) or worse because of the sum(sub) inside the loop
#Therefore we use kadane's algorithm

nums=[]
max_sum=float('-inf')
current_sum=0
for i in nums:
		current_sum+=i
		max_sum=max(max_sum,current_sum)
		if current_sum<0:
			current_sum=0
return max_sum

