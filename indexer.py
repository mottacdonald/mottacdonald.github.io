import json
import os

IGNORE = {".git", ".github", "__pycache__", "node_modules"}

REDIRECT_HTML = """<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="refresh" content="0; url=/" />
  <title>Redirecting...</title>
</head>
<body>
  <script>
    window.location.href = "/";
  </script>
</body>
</html>
"""

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


# ---------------- TREE GENERATOR ----------------


def build_tree(path):
    node = {
        "name": os.path.basename(path) if path != "." else "",
        "path": "/" + path.replace("\\", "/") if path != "." else "/",
        "type": "dir",
        "children": [],
    }

    try:
        entries = sorted(os.listdir(path))
    except:
        return node

    for e in entries:
        if e in IGNORE or e.startswith("."):
            continue

        full = os.path.join(path, e)

        if os.path.isdir(full):
            node["children"].append(build_tree(full))
        else:
            node["children"].append(
                {"name": e, "path": "/" + full.replace("\\", "/"), "type": "file"}
            )

    return node


# ---------------- INDEX.HTML GENERATION ----------------


def generate_index_htmls():
    """
    SAFE MODE:
    - only creates root index.html
    - does NOT overwrite existing files
    """

    root_index = "index.html"

    if not os.path.exists(root_index):
        with open(root_index, "w", encoding="utf-8") as f:
            f.write(VIEWER_HTML)

    print("root index.html ensured")


# ---------------- TREE ----------------


def generate_tree():
    tree = build_tree(".")

    with open("tree.json", "w", encoding="utf-8") as f:
        json.dump(tree, f, indent=2)

    print("tree.json generated")


# ---------------- FIX REDIRECT ----------------


def fix_redirect():
    removed = 0

    for root, dirs, files in os.walk("."):
        for file in files:
            if file != "index.html":
                continue

            path = os.path.join(root, file)

            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read().strip()

                if content == REDIRECT_HTML.strip():
                    os.remove(path)
                    removed += 1

            except:
                continue

    print(f"removed {removed} redirect index.html files")


# ---------------- CLI ----------------


def main():
    print("""
Commands:
1      -> generate index.html (root viewer only)
2      -> generate tree.json
temp1  -> remove redirect index.html files
exit   -> quit
""")

    while True:
        cmd = input("> ").strip()

        if cmd == "1":
            generate_index_htmls()

        elif cmd == "2":
            generate_tree()

        elif cmd == "temp1":
            fix_redirect()

        elif cmd == "exit":
            break

        else:
            print("unknown command")


if __name__ == "__main__":
    main()
