# https://leetcode.com/problems/daily-temperatures/description/
class Solution(object):
    def dailyTemperatures(self, temperatures):
        temp=len(temperatures)
        count=0
        lis=[]
        for i in range(temp):
            count=0
            flag=0
            for j in range(i+1,temp):
                count=count+1
                if temperatures[j]>temperatures[i]:
                    flag=1
                    lis.append(count)  
                    break
            if flag==0:
                lis.append(0)

               
                   
        return lis

                
                

        