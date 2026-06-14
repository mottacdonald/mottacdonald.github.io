import os
import json

IGNORE = {".git", ".github", "__pycache__", "node_modules"}

VIEWER_HTML = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>File Browser</title>
</head>
<body>
  <script src="/pages-filedisplay.js"></script>
</body>
</html>
"""


def should_ignore(path):
    parts = path.replace("\\", "/").split("/")
    return any(part in IGNORE for part in parts)


def create_index_if_missing(folder):
    index_path = os.path.join(folder, "index.html")

    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(VIEWER_HTML)
        print(f"created: {index_path}")
    else:
        print(f"skipped (exists): {index_path}")


def build_tree(folder, rel_path=""):
    node = {
        "name": os.path.basename(folder) or "/",
        "type": "dir",
        "path": "/" + rel_path.replace("\\", "/"),
        "children": []
    }

    try:
        entries = sorted(os.listdir(folder))
    except Exception:
        return node

    for entry in entries:
        if entry in IGNORE:
            continue

        full_path = os.path.join(folder, entry)
        child_rel = os.path.join(rel_path, entry).replace("\\", "/")

        if os.path.isdir(full_path):
            node["children"].append(build_tree(full_path, child_rel))
        else:
            node["children"].append({
                "name": entry,
                "type": "file",
                "path": "/" + child_rel
            })

    return node


def write_tree_json(root="."):
    tree = build_tree(root)

    with open(os.path.join(root, "tree.json"), "w", encoding="utf-8") as f:
        json.dump(tree, f, indent=2)

    print("created: tree.json")


def walk(root="."):
    for current_root, dirs, files in os.walk(root):
        if should_ignore(current_root):
            continue

        dirs[:] = [d for d in dirs if d not in IGNORE]

        create_index_if_missing(current_root)


if __name__ == "__main__":
    walk(".")
    write_tree_json(".")
    print("done")