import os

def create_file(filename, default=""):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(default)

def load_list(filename):
    items = []
    if os.path.exists(filename):
        with open(filename) as f:
            for line in f:
                items.append(line.strip().split(","))
    return items

def save_list(filename, items):
    with open(filename, "w") as f:
        for item in items:
            f.write(",".join(item) + "\n")
