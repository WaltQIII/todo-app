from functions import add_todo, show_todos, edit_todo, complete_todo
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("The time is below")
print("Is is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

    if user_action == 'add':
        add_todo()
    elif user_action == 'show':
        show_todos()
    elif user_action == 'edit':
        edit_todo()
    elif user_action == 'complete':
        complete_todo()
    elif user_action == 'exit':
        break
    else:
        print('Command not valid.')

print("Bye!")
