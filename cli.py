from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    action = input("What would you like to do? ").strip()

    if action.startswith("add"):
        action = action.removeprefix("add ") + "\n"
        todos = get_todos()

        todos.append(action)

        write_todos(todos)
    else:
        match action:
            case 'show':
                todos = get_todos()
                for index, item in enumerate(todos):
                    item = item.strip("\n")
                    print(f"{index + 1}. {item.capitalize()}")

            case 'edit':
                todos = get_todos()

                number = int(input("Which item? "))
                item = input("Enter new todo: ") + "\n"
                todos[number - 1] = item

                write_todos(todos)

            case 'complete':
                try:
                    todos = get_todos()

                    item = int(input("Which item? "))
                    todos.pop(item - 1)

                    write_todos(todos)

                    for index, item in enumerate(todos):
                        item = item.strip("\n")
                        print(f"{index + 1}. {item.capitalize()}")
                except IndexError:
                    print("That item does not exist. Please try again.")
                    continue

            case 'exit':
                break

            case _:
                print("Please enter a valid option. ")
