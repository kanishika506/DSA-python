from collections import Counter
class s:
	def isAnagram(self,s:str,t:str) -> bool:
			return Counter(t)==Counter(s)
