class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = {}
       
      for i in range(len(heights)):
            people[heights[i]]=names[i]
        
        ans=[]

        for height in sorted(people, reverse=True):
            ans.append(people[height])

        return ans
