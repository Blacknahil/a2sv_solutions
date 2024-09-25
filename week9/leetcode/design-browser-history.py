class Node:
    def __init__(self,url):
        self.url=url
        self.prev=None
        self.next=None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.home=Node(homepage)
        self.page=self.home
        

    def visit(self, url: str) -> None:
        new=Node(url)
        self.page.next=new
        new.prev=self.page
        self.page=new
        

    def back(self, steps: int) -> str:
        cur=self.page
        while cur.prev and steps:
            cur=cur.prev
            steps-=1
        self.page=cur
        return cur.url
        

    def forward(self, steps: int) -> str:
        cur=self.page
        while cur.next and steps:
            steps-=1
            cur=cur.next
        self.page=cur
        return cur.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)