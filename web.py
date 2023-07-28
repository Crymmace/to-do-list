import streamlit as st
from functions import get_todos, write_todos


def add_todo():
    new_todo = st.session_state["new_todo"]
    todos.append(new_todo)
    write_todos(todos)


todos = get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")
