class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        ans=""
        pointer=0
        while pointer < len(command):
            if command[pointer]=='G':
                ans+="G"
                pointer+=1
            elif command[pointer]=='(':
                if command[pointer + 1]==")":
                    ans+="o"
                    pointer+=2
                else:
                    ans+='al'
                    pointer+=4
        return ans

        