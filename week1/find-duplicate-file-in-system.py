class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        for info in paths:
            arr=info.split(" ")
            directory=arr[0]
            for file_info in arr[1:]:
                file_name,file_content=file_info.split("(")
                if file_content in dic:
                    dic[file_content].append("/".join([directory,file_name]))
                else:
                    dic[file_content]=["/".join([directory,file_name])]
        ans=[]
        for key in dic.keys():
            if len(dic[key])>1:
                ans.append(dic[key])
        return ans



