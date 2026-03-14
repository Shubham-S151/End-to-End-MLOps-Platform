import os

# folders to completely ignore
IGNORE_FOLDERS = {".git", "node_modules", "__pycache__", ".vscode"}

# folders to show only the name (not their contents)
NAME_ONLY_FOLDERS = {"venv"}

def print_tree(directory, prefix=""):
    items = sorted(os.listdir(directory))

    for index, item in enumerate(items):
        path = os.path.join(directory, item)
        is_last = index == len(items) - 1

        connector = "└── " if is_last else "├── "
        print(prefix + connector + item)

        # skip ignored folders
        if item in IGNORE_FOLDERS:
            continue

        # show name only (do not expand)
        if item in NAME_ONLY_FOLDERS:
            continue

        if os.path.isdir(path):
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(path, new_prefix)


if __name__ == "__main__":
    root_dir = "."
    print(os.path.basename(os.getcwd()))
    print_tree(root_dir)
