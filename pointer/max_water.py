#find two lines that together with the x-axis form a container,such that the container contains the most water
height=[]
max_area ,i=0 ,0
j=len(height)-1
while i<j:
	current_area=(j-1)*min(height[i],height[j])
	max_area=max(current_area, max_area)
	if height[i]<height[j]:
		i+=1
	else:
		j-=1
return max_area

