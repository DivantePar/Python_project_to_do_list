from appJar import gui 
import appJar
import json
import os
## This project will take user imput from a to do list 
## GUI and allow them to update it.
app = gui()
app.setFont(12)
app.setSize("Fullscreen")
# app.configure(bg='white', fg='yellow', font={'size':20, 'family':'Helvetica'})


class Count():
    def __init__(self):
        self.count = 0
    
    def getCount(self):
        return self.count
    
    def setCount(self):
        self.count +=1


def create_message(running_count, item):
    app.addMessage(str(running_count.getCount()), item)
    app.setMessageAspect(str(running_count.getCount()), 500)
    app.setMessageWidth(str(running_count.getCount()), 1000)
    running_count.setCount()


def check_json_file():
    if os.path.isfile("to_do_list.json"):
        return 
    else:
        with open("to_do_list.json", "w") as file:
            json.dump({1:"", 2:""}, file)
            return


def add_data_to_screen():
    with open("to_do_list.json", "r") as file:
        existing_data = json.load(file)
        items_list = []
        for item in existing_data.values():
            items_list.append(item)  


def submit_item(button, running_count):
    if button == "Cancel":
        app.stop()
    else:
        item = app.getEntry("Item")
        check_json_file()
        
        
        with open("to_do_list.json", "r") as file:
            starting_data = json.load(file)

            keys = list(starting_data.keys())
            
            revised_keys = [int(key) for key in keys]
            starting_data[max(revised_keys) +1] = item
        
       
        with open("to_do_list.json", "w") as file:
            json.dump(starting_data, file)

        
        
        create_message(running_count, item)
        print(running_count.getCount())

        
      
        
        # with open("to_do_list.json", "w") as file:
        #     json.dump(existing_data, file)

        add_data_to_screen()

            
def set_up_count():
    if not os.path.isfile("to_do_list.json"):
        return 
    else:
        with open("to_do_list.json", "r") as file:
            starting_data = json.load(file)
            for item in range(len(starting_data)):
                if(item > 1):
                    app.addMessage(str(running_count.getCount()), starting_data[str(item+1)])
                    app.setMessageAspect(str(running_count.getCount()), 500)
                    app.setMessageWidth(str(running_count.getCount()), 1000)
                    running_count.setCount()

running_count = Count()

app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "yellow")
app.addLabelEntry("Item")
app.addButtons(["Submit", "Cancel"], lambda button: submit_item(button, running_count))
app.addMessage("todo", "")

set_up_count()

app.go()

# print(dir(appJar.appjar))