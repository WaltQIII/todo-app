import streamlit as st
import functions

todo_filepath = 'todos.txt'

todos = functions.get_todos(todo_filepath)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

print("Hello")

st.text_input(label="", placeholder="Add new todo...")
