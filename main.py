from appJar import gui 
import appJar
import json
import os
## This project will take user imput from a to do list 
## GUI and allow them to update it.
app = gui()
app.setFont(12)


class Count():
    def __init__(self):
        self.count = 0
    
    def getCount(self):
        return self.count
    
    def setCount(self):
        self.count +=1

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
        print(existing_data)
        
        
        items_list = []
        for item in existing_data.values():
            items_list.append(item)
        
        
        app.setMessage("todo", items_list[2:])
            
            


def submit_item(button):
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

        running_count.setCount()
        print(running_count.getCount())

        
      
        
        # with open("to_do_list.json", "w") as file:
        #     json.dump(existing_data, file)

        add_data_to_screen()

            
    
running_count = Count()
app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.addLabelEntry("Item")
app.addButtons(["Submit", "Cancel"], submit_item)
app.addMessage("todo", "")

app.go()

# print(dir(appJar.appjar))