import time

FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Takes 1 arg (filepath of .txt file), reads file (or uses default value) & returns list of To-Do Items."""
    with open(filepath, 'r') as file:
        todos_og = file.readlines()
    return todos_og

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the To-Do items to a list in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

def get_action():
    user_req = input("Enter 'Add', 'Show', 'Edit', 'Complete', or 'Exit': ")
    user_req = user_req.strip()
    return user_req

def display_total():
    print(f"{'--' * 15}Total Open Tasks: {len(get_todos('todos.txt'))}{'--' * 15}")
    return

def timestamp():
    print(f"               Temporal Location: {time.strftime("%Y-%m-%d, %a | %H:%M %z")}")


if __name__ == "__main__":
    print("Hello - Running from module")
    print(get_todos())