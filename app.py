user_input = "random"
data= []


def show_menu():
    print("Menu:")
    print("1: Add an item")
    print("2: Mark as done")
    print("3: View items")
    print("4: Exit")

while user_input != "4":

    
    user_input = input("Enter your choice")

    if user_input == "1":
        item = input("what is to be done?")
        data.append(item)
        print("Added item", item)

    elif user_input == "2":
        itm = input("Remove?")
        if item in data:
            data.remove(item)
            print("Removed item",item)
        else:
            print("Item does not exist in the list")

 
    elif user_input == "3":
        print("Lit of to do items")
        for item in data:
            print(item)
        print("View the list of items")
    elif user_input == "4":
        print("Goodbye")
    else:
        print("Please enter 1,2,3 or 4")


 
