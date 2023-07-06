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









#TEST CASES AND 
#create the root directory
root=directory('ROOT')
#creating the sub_dir 
desktop=directory('DESKTOP')
video=directory('VIDEOS')
picture=directory('PICTURES')
#relating the directories : making the root the parent of all directory
root.add_dir(desktop)
root.first_child(desktop)
root.add_dir(picture)
root.add_dir(video)  
#creating files for the purpose of illustration
f1=File('video1.mp4')    
f2=File('video2.mp4')   
f3=File('video3.mp4')
f4=File('Ayda.mp3')
f5=File('bereket.mp3')
f6=File('the power of now.pdf')
f7=File('Ego is the your enemy .pdf')


#Add files to root
root.add_file(f1)
root.add_file(f2)
#add files to the sub directories 
desktop.add_file(f3)
desktop.add_file(f4)

memories=directory("MEMORIES")
picture.add_dir(memories)
picture.add_file(f5)


print(root.display())

