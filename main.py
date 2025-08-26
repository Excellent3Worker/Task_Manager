# List to store tasks
tasks = []

def show_tasks():
    if not tasks:  # if the list is empty
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['title']} - {status}")

def add_task():
    title = input("Enter the task name: ")
    tasks.append({'title': title, 'done': False})
    print(f"Task added: {title}")

def mark_done():
    show_tasks()  # first show all tasks
    index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        print(f"Task marked as done: {tasks[index]['title']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Show tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")
        choice = input("Choose an option number: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
