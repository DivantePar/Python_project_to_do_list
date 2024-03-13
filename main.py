from appJar import gui 
import appJar
import json
import os
## This project will take user imput from a to do list 
## GUI and allow them to update it.
app = gui()
app.setFont(12)



def check_json_file():
    if os.path.isfile("to_do_list.json"):
        print('hello')
        return 
    else:
        with open("to_do_list.json", "w") as file:
            json.dump([], file)
            return

def add_data_to_screen():
    with open("to_do_list.json", "r") as file:
        existing_data = json.load(file)
        the_string = ""
  
        
        for item in existing_data:
            the_string += item + " "

        app.setMessage("todo", the_string)


def submit_item(button):
    if button == "Cancel":
        app.stop()
    else:
        item = app.getEntry("Item")
        check_json_file()
        

        existing_data = [] 
        with open("to_do_list.json", "r") as file:
            for i in file:
                print(i)
                existing_data.append(i)
        
        existing_data.append(item) 



        
      
        
        with open("to_do_list.json", "w") as file:
            json.dump(existing_data, file)

        add_data_to_screen()

            
    

app.addLabel("title", "Welcome to appJar")
app.setLabelBg("title", "red")
app.addLabelEntry("Item")
app.addButtons(["Submit", "Cancel"], submit_item)
app.addMessage("todo", "")
app.go()



# print(dir(appJar.appjar))