# return True if duplicates , False otherwise

class  sol:
	def Containduplicates(self,nums:List[int]) -> bool:
			nums2=set()
			for i in nums:
				if i in nums2:
					return True
			return  False
