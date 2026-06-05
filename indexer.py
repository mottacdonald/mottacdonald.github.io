import os

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
    for bad in IGNORE:
        if bad in path:
            return True
    return False


def create_index_if_missing(folder):
    index_path = os.path.join(folder, "index.html")

    # ONLY create if missing
    if not os.path.exists(index_path):
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(VIEWER_HTML)
        print(f"created: {index_path}")
    else:
        print(f"skipped (exists): {index_path}")


def walk(root="."):
    for current_root, dirs, files in os.walk(root):
        if should_ignore(current_root):
            continue

        # skip ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE]

        create_index_if_missing(current_root)


if __name__ == "__main__":
    walk(".")
    print("done")
