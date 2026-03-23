#to find indices of element whose sum = target

class SOl:
	def  twosum(self, nums:List[],target: int) -> List[int] :
				hashmp={}
				for i , n in enumerate(nums):
							diff=target-n
							if diff in hashmp:
								return [hashmp[diff],i]								
							hashmp[n]=i
