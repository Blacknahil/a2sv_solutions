class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        reminders=[]
        while n>0:
            reminders.append(n%3)
            n=n//3
        for reminder in reminders:
            if reminder!=0 and reminder!=1:
                return False
        return True
        