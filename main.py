from appJar import gui 
import appJar
import json
import os
## This project will take user imput from a to do list 
## GUI and allow them to update it.
app = gui()
app.setFont(12)


class Count():
    count = 0

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
        


        
      
        
        # with open("to_do_list.json", "w") as file:
        #     json.dump(existing_data, file)

        add_data_to_screen()

            
    

app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.addLabelEntry("Item")
app.addButtons(["Submit", "Cancel"], submit_item)
app.addMessage("todo", "")
app.go()

# print(dir(appJar.appjar))