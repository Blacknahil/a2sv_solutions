class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        for domains in cpdomains:
             num,domain=domains.split(" ")
             num=int(num)
             dic[domain]=dic.get(domain,0) + num
             dots=domain.count(".")
             for _ in range(dots):
                 i=domain.index(".")
                 dic[domain[i+1:]]=dic.get(domain[i+1:],0) + num
                 domain=domain[i+1:]
        ans=[]
        for key in dic.keys():
            ans.append(str(dic[key]) + " " + key)
        return ans





