def get_todos(filepath):
    try:
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local
    except FileNotFoundError:
        print("File not found. Creating a new file.")
        return []


def write_todos(filepath, todos_arg):
    try:
        with open(filepath, 'w') as file:
            file.writelines(todos_arg)
    except IOError:
        print("Error writing to the file.")


def add_todo():
    todo = input("Enter new todo: ").strip()
    todos = get_todos('todos.txt')
    todos.append(todo + '\n')
    write_todos('todos.txt', todos)


def show_todos():
    todos = get_todos('todos.txt')
    for index, item in enumerate(todos):
        item = item.strip('\n')
        row = f"{index + 1}-{item}"
        print(row)


def edit_todo():
    try:
        number = int(input("Enter todo number to edit: "))
        todos = get_todos('todos.txt')
        new_todo = input("Enter new todo: ").strip()
        todos[number - 1] = new_todo + '\n'
        write_todos('todos.txt', todos)
    except ValueError:
        print('Invalid input. Please enter a number.')
    except IndexError:
        print('There is no item with that number.')


def complete_todo():
    try:
        number = int(input("Enter todo number to complete: "))
        todos = get_todos('todos.txt')
        todo_to_remove = todos.pop(number - 1).strip('\n')
        write_todos('todos.txt', todos)
        print(f'Todo {todo_to_remove} was removed from the list')
    except ValueError:
        print('Invalid input. Please enter a number.')
    except IndexError:
        print('There is no item with that number.')