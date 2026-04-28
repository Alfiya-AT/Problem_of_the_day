#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
		p=0
		res=[]
		stack=[]
		for i in str:
			if i=='(':
				p+=1
				stack.append(p)
				res.append(p)
			elif i==')':
				res.append(stack[-1])
				stack.pop()
		return res
c=Solution()
print(c.bracketNumbers(str = "(aa(bdc))p(dee)(hgh(j)"))