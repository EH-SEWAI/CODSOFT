todo = []

def show():
    if len(todo) == 0:
        print("No tasks yet.\n")
        return
    print("\nTasks:")
    for n in range(len(todo)):
        t = todo[n]
        mark = "✓" if t['done'] else " "
        print(f"{n+1}. [{mark}] {t['text']}")
    print()

def add():
    text = input("Enter task: ").strip()
    if text:
        todo.append({'text': text, 'done': False})
        print("Task added.\n")

def update():
    show()
    try:
        num = int(input("Task number to update: ")) - 1
        if 0 <= num < len(todo):
            new_text = input("New task text: ").strip()
            if new_text:
                todo[num]['text'] = new_text
                print("Task updated.\n")
    except:
        print("Error. Try again.\n")

def done():
    show()
    try:
        num = int(input("Task number to mark done: ")) - 1
        if 0 <= num < len(todo):
            todo[num]['done'] = True
            print("Marked as done.\n")
    except:
        print("Error.\n")

def delete():
    show()
    try:
        num = int(input("Task number to delete: ")) - 1
        if 0 <= num < len(todo):
            todo.pop(num)
            print("Deleted.\n")
    except:
        print("Error.\n")

# --- Main Menu ---
while True:
    print("1. Add\n2. Show\n3. Update\n4. Done\n5. Delete\n6. Exit")
    choice = input("Choose: ").strip()

    if choice == '1':
        add()
    elif choice == '2':
        show()
    elif choice == '3':
        update()
    elif choice == '4':
        done()
    elif choice == '5':
        delete()
    elif choice == '6':
        print("Bye!")
        break
    else:
        print("Not valid.\n")
