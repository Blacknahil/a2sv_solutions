class Solution:
    def smallestNumber(self, num: int) -> int:
        n_s=str(num)
        if num<0:
            n_list=list(n_s[1:])
            n_list.sort(reverse=True)
            return int("-" + "".join(n_list))
        else:
            n_list=list(n_s)
            n_list.sort()
            for i in range(len(n_list)):
                if n_list[i] !="0":
                    break
                pos=i
                while pos<len(n_list) and n_list[pos]=="0":
                    pos+=1
                if pos<len(n_list):
                    n_list[i],n_list[pos]=n_list[pos],n_list[i]
                    break
            return int("".join(n_list))

        