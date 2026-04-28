#Given a string s, find the length of the longest substring without duplicate characters.
s="abcabcacbb"
hashmp={}
left=0
max_length=0
for i , n in enumerate(s):
	if n in hashmp:
		left=max(left,hashmp[n]+1)
	hashmp[n]=i
	max_length=max(max_length,i-length+1)
return max_length

