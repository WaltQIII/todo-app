def get_todos(filepath):
    try:
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local
    except FileNotFoundError:
        return []


def write_todos(filepath, todos_arg):
    try:
        with open(filepath, 'w') as file:
            file.writelines(todos_arg)
    except IOError:
        print("Error writing to the file.")


def add_todo(filepath, new_todo):
    todos = get_todos(filepath)
    todos.append(new_todo + '\n')
    write_todos(filepath, todos)


def edit_todo(filepath, todos, todo_to_edit, new_text):
    if todo_to_edit in todos:
        index = todos.index(todo_to_edit)
        todos[index] = new_text + '\n'
        write_todos(filepath, todos)


def complete_todo(filepath, todos, todo_to_complete):
    if todo_to_complete in todos:
        todos.remove(todo_to_complete)
        write_todos(filepath, todos)
