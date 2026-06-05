import json
import os

ROOT = "."
OUTPUT_DIR = "__file_index__"

IGNORE = {".git", "__file_index__", "node_modules", ".github"}


def walk(path):
    items = []

    for name in sorted(os.listdir(path)):
        if name in IGNORE or name.startswith("."):
            continue

        full = os.path.join(path, name)
        rel = os.path.relpath(full, ROOT).replace("\\", "/")

        if os.path.isdir(full):
            items.append({"name": name, "type": "dir"})

            walk(full)

        else:
            items.append({"name": name, "type": "file"})

    os.makedirs(path, exist_ok=True)

    # write index.json per folder
    with open(os.path.join(path, "index.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

    # ONLY create index.html if it does not already exist
    index_html_path = os.path.join(path, "index.html")

    if not os.path.exists(index_html_path):
        with open(index_html_path, "w", encoding="utf-8") as f:
            f.write("""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>File Browser</title>
</head>
<body>
  <script src="/pages-filedisplay.js"></script>
</body>
</html>
""")


def main():
    walk(ROOT)
    print("Done generating index files")


if __name__ == "__main__":
    main()
