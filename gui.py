import functions
import PySimpleGUI as sg

# Specify the path to your TODOs file
todo_filepath = "C:\\Users\\Key Quarles\\PycharmProjects\\todoapp\\todos.txt"

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(todo_filepath), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")

# Window layout
layout = [
    [label],
    [input_box, add_button],
    [list_box, edit_button]
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    if values is not None:
        print(3, values['todos'])
    match event:
        case "Add":
            # Get existing todos, add the new one, and write back
            todos = functions.get_todos(todo_filepath)
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todo_filepath, todos)
            window['todos'].update(values=todos)
        case "Edit":
            # Ensure a todo is selected to edit
            selected_items = values['todos']
            if selected_items:
                todo_to_edit = selected_items[0]
                new_todo = values['todo']
                todos = functions.get_todos(todo_filepath)
                # Safely find and update the selected todo
                try:
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todo_filepath, todos)
                    window['todos'].update(values=todos)
                except ValueError:
                    sg.popup_error(f"'{todo_to_edit}' not found in todos list")
            else:
                sg.popup_error("Please select a todo to edit")
        case 'todos':
            # Update the input box to show the selected todo
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()
