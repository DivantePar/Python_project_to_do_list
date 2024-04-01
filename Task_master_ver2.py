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
        app.addLabel(str(self.running_count), item, self.running_count +4, 0)
        app.button("PRESS ME", press, colspan=2)
        app.button()

        

    
    def add_to_list(self):
        test_instances.append(self)


class Count():
    def __init__(self):
        self.count = 0
    
    def getCount(self):
        return self.count
    
    def setCount(self):
        self.count +=1


def press():
    app.label(str(randint(0, 9)), bg=app.RANDOM_COLOUR(), fg=app.RANDOM_COLOUR())


def delete_button(button_name, test_instances):
    
    for instance in test_instances:
        if "Button " + str(instance.running_count) == button_name:
            print(instance)
            print(test_instances)

            app.removeLabel(str(instance.running_count))
 

            print("Button " + str(instance.running_count))
            
            app.removeButton("Button " + str(instance.running_count))
    
            app.go()
            break
    

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


def test_class(item, running_count, test_instances):
    print("this is what is being sent", item)
    test_instances.append(Test_class(item, running_count.count))
    button_count = running_count.count  
    app.addButton("Button " + str(button_count), lambda button, btn="Button " + str(button_count): delete_button(btn, test_instances))
    running_count.setCount()
    return test_instances

            

def testing_button(button, test_instances):
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
        
        test_class(item, running_count, test_instances)

        add_data_to_screen()
        return test_instances


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
# app.addButtons(["Submit", "Cancel"], lambda button: submit_item(button, running_count))
app.addButtons(["test", "Cancel"], lambda button: testing_button(button, test_instances))
app.addMessage("todo", "")

set_up_count()

app.go()

import inspect
print(inspect.getsource(app.button))

# print(dir(appJar.appjar))