import streamlit as st
import functions

st.title("Todo List App")
st.sidebar.title("Menu")

# Define the file path
todo_filepath = 'todos.txt'

# Create a menu to select actions
menu_choice = st.sidebar.radio("Select an Action", ["View Todos", "Add Todo", "Edit Todo", "Complete Todo"])

if menu_choice == "View Todos":
    st.header("View Todos")
    todos = functions.get_todos(todo_filepath)
    for index, item in enumerate(todos):
        st.write(f"{index + 1}. {item.strip()}")

elif menu_choice == "Add Todo":
    st.header("Add Todo")
    new_todo = st.text_input("Enter new todo:")
    if st.button("Add"):
        if new_todo:
            functions.add_todo(todo_filepath, new_todo)

elif menu_choice == "Edit Todo":
    st.header("Edit Todo")
    todos = functions.get_todos(todo_filepath)
    todo_to_edit = st.selectbox("Select a todo to edit:", todos)
    new_text = st.text_input("Enter the new text:")
    if st.button("Edit"):
        functions.edit_todo(todo_filepath, todos, todo_to_edit, new_text)

elif menu_choice == "Complete Todo":
    st.header("Complete Todo")
    todos = functions.get_todos(todo_filepath)
    todo_to_complete = st.selectbox("Select a todo to complete:", todos)
    if st.button("Complete"):
        functions.complete_todo(todo_filepath, todos, todo_to_complete)
