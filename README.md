
# 📝 Python To-Do List (CLI Project)

This is a simple **Command-Line To-Do List Application** built with Python. It allows you to manage your daily tasks by adding, viewing, updating, and deleting them — all saved persistently in a `JSON` file.

---

## 📦 Features

- ➕ Add tasks with a "Pending" status
- 📋 View all current tasks with their status
- ✅ Mark tasks as "Done"
- 🗑️ Remove tasks by index
- 💾 Automatically saves your list to `todo_data.json` so your data is never lost

---

## 📁 File Structure

- `todo_data.json` – Automatically created and used to save all tasks
- `todo_list.py` – The main script file to run your To-Do list app

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.
2. Save the script as `todo_list.py`.
3. Run the program in your terminal or IDE:

```bash
python todo_list.py
```

You will see a menu:

```
📌 To-Do List Menu
1. Show tasks
2. Add task
3. Mark as Completed
4. Delete task
5. Exit the App
```

---

## 🧠 How It Works

- The program loads tasks from `todo_data.json` at startup.
- Every change (add, delete, update) is saved back to the file.
- All task information is stored as dictionaries with `Task` and `Status`.

---

## 📝 Example Entry in `todo_data.json`

```json
[
  {
    "Task": "Finish Python Project",
    "Status": "Pending"
  },
  {
    "Task": "Submit Resume",
    "Status": "Done"
  }
]
```

---

## 🚀 Future Improvements

- Add support for task deadlines or priorities
- Export tasks to CSV or PDF
- GUI version using Tkinter or PyQt
- Cloud sync support using Firebase or Google Drive

---

## 👨‍💻 Author

Created by Nitish, guided by Orion ✨  
Perfect for beginner Python projects and practical file handling practice.
