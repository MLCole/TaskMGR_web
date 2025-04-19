import streamlit as st
import os
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    if todo == "":
        pass
    else:
        todos.append(todo)
        functions.write_todos(todos)

def reload():
    del st.session_state[task]
    st.rerun()

st.title("Task MGR - ToDo App")
st.subheader("New WebApp")
st.write("This app is designed to help you get things done.")

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

for index, task in enumerate(todos):
    task = task.strip()
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)

st.text_input(label="test", placeholder="Enter a ToDo:",
              on_change=add_todo, key='new_todo', label_visibility='hidden')

st.button("Clear Completed Tasks", key='reload', on_click=reload)