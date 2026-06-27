
# Day 11 – Python `shutil` and `os` Module

## 📖 Overview
On Day 11, I learned how to manage files and folders in Python using the `shutil` and `os` modules. These modules provide powerful functions for copying, moving, renaming, and deleting files and directories.

---

## 📚 Topics Covered

### `shutil` Module
- Copy a file using `shutil.copy()`
- Copy an entire directory using `shutil.copytree()`
- Move or rename files and folders using `shutil.move()`
- Delete a directory and all its contents using `shutil.rmtree()`

### `os` Module
- Delete a file using `os.remove()`
- Delete an empty directory using `os.rmdir()`

---

## 💻 Example Code

```python
import shutil
import os

# Copy a file
shutil.copy("shutil.py", "shutil2.py")

# Copy a directory
shutil.copytree("Day11", "myDay11")

# Move or rename a file
shutil.move("shutil2.py", "backup/shutil2.py")

# Delete a file
os.remove("shutil2.py")

# Delete an empty directory
os.rmdir("empty_folder")

# Delete a directory with all its contents
shutil.rmtree("myDay11")
```

---

## 🔑 Key Functions

| Function | Description |
|----------|-------------|
| `shutil.copy()` | Copies a file |
| `shutil.copytree()` | Copies an entire directory |
| `shutil.move()` | Moves or renames a file or directory |
| `shutil.rmtree()` | Deletes a directory and all its contents |
| `os.remove()` | Deletes a file |
| `os.rmdir()` | Deletes an empty directory |

---

## 📝 Key Learnings

- `shutil` provides high-level file and directory operations.
- `os` is mainly used for interacting with the operating system.
- `os.remove()` deletes only files.
- `os.rmdir()` deletes only empty directories.
- `shutil.rmtree()` removes non-empty directories.
- `shutil.move()` can be used to both move and rename files or folders.

---

## 🎯 Learning Outcome

By the end of Day 11, I understood how to:
- Copy files and directories.
- Move and rename files or folders.
- Delete files and directories safely.
- Choose between the `os` and `shutil` modules based on the task.

---

### 🚀 Tech Stack
- Python 3
- `os` Module
- `shutil` Module

---
⭐ Part of my **Python Learning Journey**.
