import json
import os

ROOT = "."


def scan_dir(path):
    items = []

    for name in sorted(os.listdir(path)):
        full = os.path.join(path, name)

        # skip hidden files + script itself
        if name.startswith(".") or name == "generate_indexes.py":
            continue

        if os.path.isdir(full):
            items.append({"name": name, "type": "dir"})

            # recurse
            scan_dir(full)

        else:
            items.append({"name": name, "type": "file"})

    # write index.json
    with open(os.path.join(path, "index.json"), "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2)

    # optional index.html (only if missing)
    index_html = os.path.join(path, "index.html")
    if not os.path.exists(index_html):
        with open(index_html, "w", encoding="utf-8") as f:
            f.write("""<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>File Browser</title>
</head>
<body>
  <script src="/js/pages-filedisplay.js"></script>
</body>
</html>
""")


def main():
    scan_dir(ROOT)
    print("Done generating index.json files")


if __name__ == "__main__":
    main()
