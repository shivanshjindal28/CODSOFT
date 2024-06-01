import sys

# Define the To-Do list
todo_list = []

def show_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Remove To-Do Item")
    print("4. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour To-Do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, item in enumerate(todo_list, start=1):
            print(f"{index}. {item}")

def add_todo_item():
    item = input("\nEnter a new To-Do item: ")
    todo_list.append(item)
    print(f"'{item}' has been added to your To-Do list.")

def remove_todo_item():
    view_todo_list()
    if todo_list:
        try:
            index = int(input("\nEnter the number of the item to remove: "))
            if 0 < index <= len(todo_list):
                removed_item = todo_list.pop(index - 1)
                print(f"'{removed_item}' has been removed from your To-Do list.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice: ")
        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_todo_item()
        elif choice == '3':
            remove_todo_item()
        elif choice == '4':
            print("Exiting the To-Do List Application.")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
