from appJar import gui 
import appJar
import json
import os


app = gui()
app.setFont(12)
app.setSize("Fullscreen")
# app.configure(bg='white', fg='yellow', font={'size':20, 'family':'Helvetica'})

test_instances = []

class Test_class():
    def __init__(self,item, running_count):
        self.running_count = running_count
        # self.id = len(test_instances)
        app.addMessage(str(self.running_count), item)
        app.setMessageLocation(str(self.running_count), 2, 3)
        app.setMessageFg(str(self.running_count), "blue")
        app.setMessageBg(str(self.running_count), "yellow")
        app.setMessageAspect(str(self.running_count), 500)
        app.setMessageWidth(str(self.running_count), 1000)
    
    def add_to_list(self):
        test_instances.append(self)


class Count():
    def __init__(self):
        self.count = 0
    
    def getCount(self):
        return self.count
    
    def setCount(self):
        self.count +=1