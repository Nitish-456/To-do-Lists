import json
import os

FILENAME = "todo_data.json"
To_do_lists = []

# 🔃 Load existing tasks from file (if any)


def load_tasks():
    global To_do_lists
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            To_do_lists = json.load(file)
    else:
        To_do_lists = []

# 💾 Save current tasks to file


def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(To_do_lists, file, indent=4)

# ✅ Show all tasks


def show_task():
    print("\n📋 Your To-Do List:")
    if len(To_do_lists) == 0:
        print("Your To-Do list is empty!")
    else:
        for index, task in enumerate(To_do_lists, 1):
            print(f"{index}. {task['Task']} - [{task['Status']}]")

# ➕ Add a new task


def add_task():
    task = input("Enter your Task: ").strip()
    To_do_lists.append({"Task": task, "Status": "Pending"})
    save_tasks()
    print("✅ New task added successfully!")

# ✅ Mark a task as done


def update_task():
    if len(To_do_lists) == 0:
        print("List is empty.")
    else:
        try:
            index = int(input("Enter task number to mark as done: ")) - 1
            if 0 <= index < len(To_do_lists):
                To_do_lists[index]['Status'] = 'Done'
                save_tasks()
                print(f"✅ Task '{To_do_lists[index]['Task']}' marked as Done.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

# 🗑️ Remove a task


def remove_task():
    if len(To_do_lists) == 0:
        print("List is empty.")
    else:
        try:
            index = int(input("Enter task number to delete: ")) - 1
            if 0 <= index < len(To_do_lists):
                removed = To_do_lists.pop(index)
                save_tasks()
                print(f"🗑️ Task '{removed['Task']}' removed.")
            else:
                print("❌ Invalid task number.")
        except ValueError:
            print("❌ Please enter a valid number.")

# 🧠 Main menu loop


def main():
    load_tasks()  # ✅ Load saved tasks at startup

    while True:
        print("\n📌 To-Do List Menu")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark as Completed")
        print("4. Delete task")
        print("5. Exit the App")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            update_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1–5.")


main()
