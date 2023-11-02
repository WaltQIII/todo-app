import functions
import PySimpleGUI as sg

# Specify the path to your TODOs file
todo_filepath = "C:\\Users\\Key Quarles\\PycharmProjects\\todoapp\\todos.txt"

# Window layout
layout = [
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("Add")],
    [sg.Listbox(values=functions.get_todos(todo_filepath), key='todos', enable_events=True, size=(45, 10)),
     sg.Button("Edit"), sg.Button("Complete")],
    [sg.Button("Exit")]
]

window = sg.Window('My To-Do App', layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    if values is not None:
        print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos(todo_filepath)
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_todos(todo_filepath, todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')  # Clear input box
        case "Edit":
            selected_items = values['todos']
            if selected_items:
                todo_to_edit = selected_items[0]
                new_todo = values['todo']
                todos = functions.get_todos(todo_filepath)
                try:
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todo_filepath, todos)
                    window['todos'].update(values=todos)
                    window['todo'].update(value='')  # Clear input box
                except ValueError:
                    sg.popup_error(f"'{todo_to_edit}' not found in todos list", font=("Helvetica", 20))
            else:
                sg.popup_error("Please select a todo to edit")
        case "Complete":
            selected_items = values['todos']
            if selected_items:
                todo_to_complete = selected_items[0]
                todos = functions.get_todos(todo_filepath)
                todos.remove(todo_to_complete)
                functions.write_todos(todo_filepath, todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')  # Clear input box
            else:
                sg.popup_error("Please select a todo to complete")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])

window.close()
