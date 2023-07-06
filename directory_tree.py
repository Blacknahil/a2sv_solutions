class directory:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.next_sibiling=None
        self.prev_sibiling=None
        self.first_child=None
    def add_dir(self,dir):
        dir.parent=self
        if self.first_child is None:
            self.first_child=dir
        else:
            current_child=self.first_child
            while current_child.next_sibiling is not None:
                current_child=current_child.next_sibiling
            current_child.next_sibiling=dir
            dir.prev_sibiling=current_child
    def add_file(self,file):
        file.parent=self
        if self.first_child is None:
            self.first_child=file
        else:
            current_child=self.first_child
            while current_child.next_sibiling is not None:
                current_child=current_child.next_sibiling
            current_child.next_sibiling=file
            file.prev_sibiling=current_child
    
    def display(self,indent=0):
        print('  '* indent +self.data + '/')
        current_child=self.first_child
        while current_child is None:
            if isinstance(current_child,dir):
                current_child.display(indent+4)
            else:
                print(" " * (indent+4)+ current_child)
                current_child=current_child.next_sibiling
    
    
class File:
     def __init__(self,data):
            self.data=data
            self.parent=None
            self.next_sibiling=None
            self.prev_sibiling=None
